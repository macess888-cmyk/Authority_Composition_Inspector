# CHECKPOINT 020 — HYBRID PUBLICATION PIPELINE VERIFICATION

**Status:** VERIFIED / FROZEN

## Purpose

This checkpoint records successful end-to-end verification of the local hybrid evidence-to-publication pipeline.

## Verified pipeline

Graphviz:

Graphviz source
-> SVG
-> Inkscape PDF conversion

Mermaid:

Mermaid source
-> Mermaid CLI PNG render

Publication:

Markdown source
-> PDF-safe Markdown
-> Pandoc
-> XeLaTeX
-> final PDF
-> SHA-256 receipt

## Governing sequence

Evidence
-> Structure
-> Graph
-> Render
-> Publication

## Renderer-specific boundary

The pipeline does not assume one conversion path works equally for every renderer.

Observed behavior:

- Graphviz SVG converted successfully through Inkscape to PDF.
- Mermaid SVG contained SVG features such as foreignObject that did not survive the Inkscape conversion path correctly.
- Mermaid CLI direct PNG rendering preserved the Mermaid node labels and produced a tightly bounded render suitable for Pandoc/XeLaTeX.
- Renderer-specific handling was therefore required.

Renderer equivalence was not assumed.

## Final artifact

Path:

C:\Users\maces\.workstation-observatory\renders\hybrid_pipeline_report.pdf

Size:

42804 bytes

SHA-256:

DCD9CC6AEF6B25EF5936EC3800F35784C1660D293B0AD379BC2EB6D6A1CDD3B2

## Visual verification

Final PDF contains:

- Hybrid Pipeline Report heading
- evidence-to-publication sequence
- labeled Graphviz pipeline
- labeled Mermaid pipeline
- both figures on one page
- figure captions preserved

## Environment verified

- Pandoc available
- MiKTeX available
- XeLaTeX available
- Inkscape 1.4.4 available
- Mermaid CLI available
- Graphviz available

## Repository state before checkpoint

Branch:

master

Remote:

origin/master synchronized

Working tree:

clean

## Established result

The local workstation can produce a deterministic publication artifact through a hybrid renderer pipeline.

This establishes:

render path exists

!=

all renderers require the same transformation path

and:

artifact exists

!=

artifact integrity recorded

The SHA-256 receipt preserves the final publication artifact identity.

## Freeze posture

Do not modify the verified renderer pipeline merely for uniformity.

Only reopen this checkpoint if:

- a renderer fails,
- an artifact changes unexpectedly,
- reproducibility fails,
- integrity verification fails,
- or a genuinely new publication boundary is identified.
