"""Apply the sourced, chapter-specific epigraph selections to canonical text."""
import gzip
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
AUDIT = Path(__file__).resolve().parent
BASE = json.loads(gzip.decompress((AUDIT / 'before-sources.json.gz').read_bytes()))
BLOCK = re.compile(r'^::: \{#chapter-(\d{2})-start \.chapter-epigraph\}\n.*?\n:::', re.M | re.S)


def entry(number, quote, author, title, url, date, genre, fit):
    return dict(chapter=number, quote=quote, author=author, title=title,
                url=url, date_and_locator=date, genre=genre, fit=fit)


SELECTIONS = [
    entry(1, 'For to be possessed of a vigorous mind is not enough; the prime requisite is rightly to apply it.', 'René Descartes', '*Discourse on the Method*', 'https://www.gutenberg.org/cache/epub/59/pg59-images.html', '1637, Part I, translated by John Veitch', 'philosophy book', 'Distinguishes having intellectual ability from using a sound decision process.'),
    entry(2, 'Plans are worthless, but planning is everything.', 'Dwight D. Eisenhower', 'remarks at the National Defense Executive Reserve Conference', 'https://www.eisenhowerlibrary.gov/eisenhowers/quotes', '14 November 1957', 'speech', 'Introduces preparation, alternatives, and robustness without treating a plan as a guarantee.'),
    entry(4, 'As a man is, so he sees. As the eye is formed, such are its powers.', 'William Blake', 'letter to the Reverend John Trusler', 'https://en.wikisource.org/wiki/Page:The_letters_of_William_Blake_%281906%29.djvu/120', '23 August 1799', 'letter', 'Expresses the contribution of the perceiver to perception.'),
    entry(5, 'The difference between a lady and a flower girl is not how she behaves, but how she’s treated.', 'George Bernard Shaw', '*Pygmalion*', 'https://www.gutenberg.org/cache/epub/3825/pg3825-images.html', '1916, Act V', 'play', 'Connects social expectations and treatment with the person someone becomes.'),
    entry(7, 'The head is ever the dupe of the heart.', 'François de La Rochefoucauld', '*Maxims*', 'https://www.gutenberg.org/files/9105/9105-h/9105-h.htm', '1665, maxim 102, translated by J. W. Willis Bund and J. Hain Friswell', 'literary maxims', 'Introduces the possibility that reasons serve motives rather than reveal them.'),
    entry(8, 'The heart has its reasons, which reason does not know.', 'Blaise Pascal', '*Pensées*', 'https://www.gutenberg.org/cache/epub/18269/pg18269-images.html', '1670, §277, translated by W. F. Trotter', 'philosophy book', 'Provides an accessible invitation to examine intuitive and deliberate judgment.'),
    entry(9, 'We suffer more often in imagination than in reality.', 'Seneca', '*Moral Letters to Lucilius*', 'https://en.wikisource.org/wiki/Moral_letters_to_Lucilius/Letter_13', 'letter 13, §4, translated by Richard M. Gummere, 1917', 'philosophical letters', 'Connects vivid imagined events and feelings with perceived danger.'),
    entry(11, 'Nowadays people know the price of everything and the value of nothing.', 'Oscar Wilde', '*The Picture of Dorian Gray*', 'https://www.gutenberg.org/cache/epub/174/pg174-images.html', '1891, ch. IV', 'novel', 'Raises the distinction between a visible price cue and the value assigned to an option.'),
    entry(12, 'There is nothing either good or bad but thinking makes it so.', 'William Shakespeare', '*Hamlet*', 'https://www.folger.edu/explore/shakespeares-works/hamlet/read/2/2/', 'c. 1600, Act II, scene ii', 'play', 'Introduces the role of interpretation in evaluation.'),
    entry(13, 'Sixty-two thousand four hundred repetitions make one truth.', 'Aldous Huxley', '*Brave New World*', 'https://huxleyarchive.org/Fiction/COVERS/Brave%20New%20World.pdf', '1932, ch. III', 'novel', 'A fictional image of repetition becoming apparent truth, fitting familiarity and fluency.'),
    entry(14, 'The great tragedy of Science—the slaying of a beautiful hypothesis by an ugly fact.', 'Thomas Henry Huxley', '“Biogenesis and Abiogenesis”', 'https://aleph0.clarku.edu/huxley/CE8/B-Ab.html', 'presidential address to the British Association, 1870', 'speech', 'Highlights revising a favored belief in response to evidence.'),
    entry(15, 'I can live with doubt and uncertainty and not knowing.', 'Richard P. Feynman', '*The Pleasure of Finding Things Out*', 'https://www.richardfeynman.com/about/quote.html', 'BBC interview, 1981', 'interview', 'Introduces calibration and the willingness to acknowledge uncertainty.'),
    entry(16, 'Life is either a daring adventure or nothing.', 'Helen Keller', 'quotation preserved by the American Foundation for the Blind', 'https://www.afb.org/fun-facts-and-quotes', '1941', 'archived literary quotation', 'Provides a memorable opening to the tension between opportunity and risk.'),
    entry(17, '’Tis better to have loved and lost than never to have loved at all.', 'Alfred, Lord Tennyson', '*In Memoriam A. H. H.*', 'https://www.poetryfoundation.org/poems/45336/in-memoriam-a-h-h-obiit-mdcccxxxiii-27', '1850, canto XXVII', 'poem', 'Contrasts a loss after a gain with never having the gain, inviting reflection on reference points and experience.'),
    entry(18, 'We should be careful to get out of an experience only the wisdom that is in it—and stop there.', 'Mark Twain', '*Following the Equator*', 'https://www.gutenberg.org/cache/epub/2895/pg2895-images.html', '1897, ch. XI', 'travel memoir', 'Warns against drawing more from a limited experience than it can establish.'),
    entry(19, 'I can resist everything except temptation.', 'Oscar Wilde', '*Lady Windermere’s Fan*', 'https://www.gutenberg.org/cache/epub/790/pg790-images.html', '1892, Act I', 'play', 'Captures the conflict between a plan and an immediately attractive option.'),
    entry(20, 'A small leak will sink a great ship.', 'Benjamin Franklin', '*The Way to Wealth*', 'https://www.gutenberg.org/files/43855/43855-h/43855-h.htm', '1758', 'popular advice essay', 'Connects everyday spending categories and small expenditures with the overall budget.'),
    entry(21, 'All our life, so far as it has definite form, is but a mass of habits.', 'William James', '*Talks to Teachers on Psychology*', 'https://www.gutenberg.org/files/16287/16287-h/16287-h.htm', '1899, ch. VIII', 'public lectures', 'Gives a direct, memorable account of the place of habits in daily life.'),
    entry(22, 'Tell me, what is it you plan to do with your one wild and precious life?', 'Mary Oliver', '“The Summer Day”', 'https://poets.org/poem/summer-day', '1990', 'poem', 'Invites the reader to connect decisions with the life they want to live.'),
    entry(23, 'Now, here, you see, it takes all the running you can do, to keep in the same place.', 'Lewis Carroll', '*Through the Looking-Glass*', 'https://www.gutenberg.org/cache/epub/12/pg12-images.html', '1871, ch. II', 'novel', 'Uses the Red Queen’s moving world to introduce outcomes that depend on other actors and changing conditions.'),
    entry(24, 'Alone we can do so little; together we can do so much.', 'Helen Keller', 'vaudeville performance script', 'https://afb.org/about-afb/history/helen-keller/quotes/helen-keller-quotes-progress', 'c. 1920', 'performance script', 'Opens the chapter with the value of coordinating actions.'),
    entry(25, 'We are all caught in an inescapable network of mutuality.', 'Martin Luther King Jr.', 'remarks at the Africa Freedom Dinner', 'https://kinginstitute.stanford.edu/king-papers/documents/remarks-delivered-africa-freedom-dinner-atlanta-university', '13 May 1959', 'speech', 'Connects interdependence, common identity, and cooperation beyond a narrow group.'),
    entry(26, 'Whoso would be a man must be a nonconformist.', 'Ralph Waldo Emerson', '“Self-Reliance”', 'https://www.gutenberg.org/cache/epub/16643/pg16643-images.html', '1841', 'literary essay', 'Introduces the tension between independent judgment and pressure to conform.'),
    entry(27, 'We simply attempt to be fearful when others are greedy and to be greedy only when others are fearful.', 'Warren Buffett', '1986 letter to Berkshire Hathaway shareholders', 'https://www.berkshirehathaway.com/letters/1986.html', '27 February 1987', 'shareholder letter', 'Connects market sentiment, imitation, and mispricing.'),
    entry(28, 'Power tends to corrupt and absolute power corrupts absolutely.', 'Lord Acton', 'letter to Mandell Creighton', 'https://oll.libertyfund.org/titles/acton-acton-creighton-correspondence', '5 April 1887', 'letter', 'Raises the problem of authority without effective challenge or accountability.'),
    entry(29, 'Every one gives the title of barbarism to everything that is not in use in his own country.', 'Michel de Montaigne', '“Of Cannibals,” *Essays*', 'https://www.gutenberg.org/cache/epub/3600/pg3600-images.html', '1580, Book I, ch. XXX; Charles Cotton translation revised by W. Carew Hazlitt, 1877', 'literary essay', 'Introduces judging unfamiliar practices through one’s own cultural standards.'),
    entry(30, 'If you would win a man to your cause, first convince him that you are his sincere friend.', 'Abraham Lincoln', 'address to the Springfield Washington Temperance Society', 'https://www.abrahamlincolnonline.org/lincoln/speeches/temperance.htm', '22 February 1842', 'speech', 'Connects persuasion with trust and sincere concern for the listener.'),
    entry(31, 'We tell ourselves stories in order to live.', 'Joan Didion', '*The White Album*', 'https://www.joandidion.org/joan-didion-books/the-white-album', '1979, opening essay', 'literary essays', 'Introduces narrative as a way of organizing experience rather than as a guarantee of truth.'),
    entry(33, 'If thought corrupts language, language can also corrupt thought.', 'George Orwell', '“Politics and the English Language”', 'https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/', '1946', 'public essay', 'Introduces the two-way relationship between language and interpretation.'),
    entry(34, 'Listening is where love begins: listening to ourselves and then to our neighbors.', 'Fred Rogers', '*The World According to Mister Rogers*', 'https://www.fredrogersinstitute.org/resources/reflections-on-fred-rogers-healing-power-of-presence', '2003, p. 93', 'popular book', 'Connects attentive listening with care and relationship repair.'),
    entry(37, 'If you want to make peace with your enemy, you have to work with your enemy. Then he becomes your partner.', 'Nelson Mandela', '*Long Walk to Freedom*', 'https://www.mpm.edu/sites/default/files/images/exhibitions/special/mandela/edu%20pdfs/Intro%20to%20Nelson%20Mandela%20%28Powerpoint%29.pdf', '1994, quoted in the official Mandela exhibition', 'autobiography', 'Introduces the move from opposition toward joint work and mutually useful agreements.'),
    entry(39, 'For the great doesn’t happen through impulse alone, and is a succession of little things that are brought together.', 'Vincent van Gogh', 'letter to Theo van Gogh', 'https://vangoghletters.org/vg/letters/let274/letter.html', '22 October 1882, letter 274', 'letter', 'Connects sustained change with assembling small actions into a workable routine.'),
    entry(40, 'We shape our buildings, and afterwards our buildings shape us.', 'Winston Churchill', 'speech on rebuilding the House of Commons', 'https://heritagecollections.parliament.uk/exhibits/rebuilding/', '28 October 1943', 'speech', 'Expresses the central role of environments in shaping behavior.'),
    entry(41, 'What is wanted is not the will to believe, but the wish to find out, which is its exact opposite.', 'Bertrand Russell', '*Free Thought and Official Propaganda*', 'https://www.gutenberg.org/files/44932/44932-h/44932-h.htm', 'Conway Memorial Lecture, 24 March 1922', 'public lecture', 'Connects decision procedures with inquiry and correction rather than defending a favored answer.'),
    entry(42, 'We will need intelligent machines to help us turn our grandest dreams into reality.', 'Garry Kasparov', '“Don’t Fear Intelligent Machines. Work with Them”', 'https://blog.ted.com/humans-must-face-our-fears-garry-kasparov-speaks-at-ted2017/', 'TED talk, 24 April 2017', 'public talk', 'Introduces machines as resources for pursuing human purposes.'),
]

RETAINED = {
    3: ('psychology book', 'Short, recognizable insight about selective attention.'),
    6: ('philosophy book', 'Memorable distinction between reasoning and the ends that motivate choice; the body explicitly discusses this epigraph.'),
    10: ('philosophy book', 'A clear historical statement of confirmation bias.'),
    32: ('commencement speech', 'A famous, accessible warning about fooling oneself.'),
    35: ('economics book', 'A direct, memorable account of reciprocal exchange.'),
    36: ('classical strategy book', 'Connects preparation with bargaining and strategic action.'),
    38: ('political philosophy book', 'Highlights the importance of making agreements enforceable.'),
}


def main():
    selected = {e['chapter']: e for e in SELECTIONS}
    records = []
    for source, before in BASE.items():
        if not source.startswith('chapters/'):
            continue
        matches = list(BLOCK.finditer(before))
        assert len(matches) == 1, source
        match = matches[0]
        number = int(match[1])
        old_quote = re.search(r'^> “(.+)”$', match[0], re.M)[1]
        old_attribution = re.search(r'^> — (.+)$', match[0], re.M)[1]
        if number in selected:
            item = selected[number].copy()
            attribution = f"{item['author']}, [{item['title']}]({item['url']}), {item['date_and_locator']}"
        else:
            genre, fit = RETAINED[number]
            item = dict(chapter=number, quote=old_quote, genre=genre, fit=fit)
            attribution = old_attribution
            if number == 3:
                attribution = attribution.replace('https://psychclassics.yorku.ca/James/Principles/prin11.htm', 'https://www.gutenberg.org/cache/epub/57628/pg57628-images.html')
            elif number == 32:
                attribution = 'Richard P. Feynman, [“Cargo Cult Science”](https://calteches.library.caltech.edu/51/2/CargoCult.htm), Caltech commencement address, 1974'
            elif number == 36:
                attribution = attribution.replace('https://www.gutenberg.org/files/66706/old/old/66706-h.htm', 'https://www.gutenberg.org/cache/epub/132/pg132-images.html')
        quote = item['quote']
        assert len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", quote)) <= 25, (number, quote)
        block = f'::: {{#chapter-{number:02d}-start .chapter-epigraph}}\n> “{quote}”\n>\n> — {attribution}\n:::'
        after = before[:match.start()] + block + before[match.end():]
        current = (ROOT / source).read_text()
        assert current in (before, after), f'Unexpected source change: {source}'
        if current != after:
            (ROOT / source).write_text(after)
        records.append(dict(item, source=source, original_quote=old_quote,
                            original_attribution=old_attribution, attribution=attribution,
                            before=match[0], after=block, changed_quote=quote != old_quote,
                            changed_block=block != match[0]))
    assert len(records) == 42
    assert len(SELECTIONS) + len(RETAINED) == 42
    records.sort(key=lambda e: e['chapter'])
    (AUDIT / 'epigraph-selections.json').write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n')
    print(f"Reviewed {len(records)} epigraphs; replaced {sum(r['changed_quote'] for r in records)} quotations; updated {sum(r['changed_block'] for r in records)} opening blocks.")


if __name__ == '__main__':
    main()
