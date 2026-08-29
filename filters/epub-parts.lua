-- Keep explicit Part pages in the EPUB reading order without counting them as chapters.
function Header(header)
  if header.level ~= 1 then
    return nil
  end

  local title = pandoc.utils.stringify(header.content)
  if title:match("^Part%s+[IVXLCDM]+%.") or title:match("^Applied%s+Interlude%.") then
    header.classes:insert("unnumbered")
    return header
  end

  return nil
end
