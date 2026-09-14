# Maintaining this site

Everything is one HTML file (`index.html`) and one stylesheet
(`assets/css/style.css`). There is no build step — you edit the HTML
directly, commit, and push. GitHub Pages republishes automatically,
usually within a minute or two.

If you're not comfortable editing HTML by hand yet, that's fine: every
block below shows you exactly what to copy, and where.

## Add a published paper

Open `index.html` and find `<h3>Peer-Reviewed</h3>`. Copy one `<li
class="pub">...</li>` block (an existing one is a safe template) and
paste a new copy directly above or below it, inside the same `<ol
class="pub-list">`. Then edit, inside your new copy:

- `pub-title`: authors in submission order, **your name in bold**
  (`<strong>Faisal Mahmud</strong>`), the paper title in curly quotes,
  and a `<span class="tag">Published</span>` tag.
- `pub-meta`: venue, year, page numbers, acceptance rate if you have a
  source for it.
- `pub-finding`: one plain-language sentence — what did you find, why
  should a reader care. Not the abstract.
- `pub-links`: PDF, DOI, code, slides, poster, talk video — whatever
  exists. Delete `<li>` entries for links that don't exist yet; don't
  leave dead links in.

## Add a manuscript that isn't published yet

Same as above, but paste your copy inside `<h3>Manuscripts Under
Submission &amp; In Preparation</h3>` instead, and keep the
`<span class="tag tag-preprint">Manuscript &middot; unpublished</span>`
tag. Never change an unpublished entry's tag to `tag` (published) until
it has actually been accepted — that distinction is the whole point of
having two sections.

When a manuscript from that section gets accepted: cut its `<li>` block
out of the "Manuscripts" list, paste it into "Peer-Reviewed" instead,
update the tag to `Published`, and fill in the real venue/year/pages/DOI.

## Add a news item

Find `<section id="news">` and its `<ul>`. Add a new `<li>` at the
**top** of the list (newest first):

```html
<li><time datetime="2027-01">Jan 2027</time> &mdash; Your update here.</li>
```

Keep the `datetime` attribute in `YYYY-MM` format — it's what lets
search engines and any future tooling parse the date, even though only
the human-readable text next to it is shown.

## Update the CV PDF

1. Export your CV to PDF with your usual tool (make sure it has no
   `[bracketed placeholder]` text left in it — this file is linked
   directly with nothing in front of it).
2. Replace `cv/faisal-mahmud-cv.pdf` with the new file, keeping the
   exact same filename so the link on the site keeps working.
3. Commit and push (see the git commands in the setup instructions you
   were given separately). If you ever want the link to show a
   "last updated" date, say so and it's a one-line change to
   `index.html`.

## Remove the News section entirely

If you decide you don't want a News section: delete the whole block in
`index.html` starting at `<section id="news" aria-labelledby="news-h">`
and ending at its matching `</section>`, then delete the
`<li><a href="#news">News</a></li>` line from the nav near the top of
the file.

## Filling in the rest of the TODOs

Search `index.html` for the text `TODO(faisal)` — every one is a
visible orange/tan callout box on the live page (so you can't ship it
by accident) with instructions for what to write. Once you've replaced
the content around a TODO block, delete the `<div class="todo">...
</div>` box itself; it's not meant to stay on the live site.

## Local preview before pushing

From inside the project folder:

```
python3 -m http.server 8000
```

Then open `http://localhost:8000/` in your browser. Press Ctrl+C in the
terminal to stop the server when you're done. Refresh the page after
every save to see your change.

## Checking you haven't broken anything

- Every internal link should be a relative path (`cv/...`,
  `assets/...`, `#section-id`) — those work locally and on GitHub
  Pages without changes.
- If you add an image, give it real `alt` text describing what it
  shows (or `alt=""` if it's purely decorative).
- Don't add a `<script src="https://...">` or `<link
  href="https://fonts...">` tag pointing at any external host — that's
  the one rule this site is built around not breaking.
