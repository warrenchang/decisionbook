/* Local, accessible practice sets. No network requests or response persistence. */
(() => {
  'use strict';
  document.querySelectorAll('form.book-practice').forEach(form => {
    if (form.dataset.initialized) return;
    const questions = [...form.querySelectorAll('fieldset.practice-question')];
    const answers = [...form.querySelectorAll('.practice-answer-list > li')];
    if (!questions.length || answers.length !== questions.length) return;
    const key = form.querySelector('.practice-key');
    const submit = form.querySelector('.practice-submit');
    const retry = form.querySelector('.practice-retry');
    const progress = form.querySelector('.practice-progress');
    const score = form.querySelector('.practice-score');
    let complete = false;
    const selected = q => q.querySelector('input:checked');
    const update = () => {
      const count = questions.filter(selected).length;
      progress.textContent = `${count} of ${questions.length} answered`;
      submit.disabled = complete || count !== questions.length;
    };
    key.hidden = true;
    form.dataset.initialized = 'true';
    form.addEventListener('change', update);
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (complete) return;
      const firstMissing = questions.find(q => !selected(q));
      if (firstMissing) {
        firstMissing.querySelector('input').focus();
        update();
        return;
      }
      let correct = 0;
      questions.forEach((q, index) => {
        const choice = selected(q);
        const answer = Number(answers[index].dataset.answer);
        const passed = Number(choice.value) === answer;
        if (passed) correct++;
        const result = q.querySelector('.practice-item-result');
        result.textContent = passed ? 'Correct.' : `Your answer: ${'ABCDE'[Number(choice.value)]}. Correct answer: ${'ABCDE'[answer]}.`;
        result.hidden = false;
        q.dataset.result = passed ? 'correct' : 'incorrect';
        q.querySelectorAll('input').forEach(input => { input.disabled = true; });
        const your = answers[index].querySelector('.practice-your-answer');
        your.textContent = `Your answer: ${'ABCDE'[Number(choice.value)]} — ${passed ? 'correct' : 'incorrect'}.`;
        your.hidden = false;
      });
      complete = true;
      score.textContent = `You answered ${correct} of ${questions.length} correctly. Review the explanations below, then try the set again when ready.`;
      score.hidden = false;
      key.hidden = false;
      key.open = true;
      retry.hidden = false;
      submit.hidden = true;
      update();
      score.focus();
    });
    retry.addEventListener('click', () => {
      form.reset();
      complete = false;
      key.hidden = true;
      key.open = false;
      score.hidden = true;
      retry.hidden = true;
      submit.hidden = false;
      questions.forEach(q => {
        delete q.dataset.result;
        q.querySelector('.practice-item-result').hidden = true;
        q.querySelectorAll('input').forEach(input => { input.disabled = false; });
      });
      answers.forEach(a => { a.querySelector('.practice-your-answer').hidden = true; });
      update();
      questions[0].querySelector('input').focus();
    });
    // Discard any selections restored by the browser after reload or back navigation.
    const resetRestored = () => { if (!complete) { form.reset(); update(); } };
    window.addEventListener('pageshow', resetRestored);
    resetRestored();
  });
})();
