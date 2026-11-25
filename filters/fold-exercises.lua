-- Leave exercise headings available to the table of contents and fold their bodies.
local summaries = {
  ["Chapter practice"] = "Open practice questions",
  ["Practice questions"] = "Open review questions",
  ["Study and practice"] = "Open study questions",
  ["Transfer exercise"] = "Open exercise",
}

local function exercise_summary(header)
  local title = pandoc.utils.stringify(header.content)
  if title == "Practice Lab" or title:match("^Practice Lab:") or title:match("^Practice:") then
    return "Open exercise"
  end
  return summaries[title]
end

function Pandoc(doc)
  local blocks = pandoc.List()
  local exercise
  local summary

  local function finish_exercise()
    if exercise and #exercise > 0 then
      blocks:insert(pandoc.RawBlock("html",
        '<details class="exercise-disclosure"><summary>' .. summary .. '</summary>'))
      -- Group nested headings so their section tags stay inside the disclosure.
      blocks:insert(pandoc.Div(exercise))
      blocks:insert(pandoc.RawBlock("html", "</details>"))
    end
    exercise = nil
  end

  for _, block in ipairs(doc.blocks) do
    if block.t == "Header" and block.level <= 2 then
      finish_exercise()
      blocks:insert(block)
      if block.level == 2 then
        summary = exercise_summary(block)
        if summary then
          exercise = pandoc.List()
        end
      end
    elseif exercise then
      exercise:insert(block)
    else
      blocks:insert(block)
    end
  end

  finish_exercise()
  doc.blocks = blocks
  return doc
end
