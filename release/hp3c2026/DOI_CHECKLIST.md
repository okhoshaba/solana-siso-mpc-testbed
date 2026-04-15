# HP3C 2026 DOI Checklist

## Before Release

- [ ] Verify the paper-facing artifact is frozen for the HP3C 2026 release.
- [ ] Verify the canonical dataset path is final: `raw_selected -> processed -> results -> figures`.
- [ ] Verify the manuscript refers to the artifact and its paper-facing path consistently.
- [ ] Create or confirm the Git tag / GitHub release for the HP3C 2026 artifact snapshot.
- [ ] Ensure GitHub-Zenodo integration is enabled, or prepare a manual Zenodo upload.
- [ ] Review Zenodo metadata one final time before publication.

## DOI Minting Flow

- [ ] Publish the archival release.
- [ ] Confirm the Zenodo metadata before minting the DOI.
- [ ] Obtain the minted DOI.
- [ ] Update manuscript artifact citation text to use the DOI.
- [ ] Rebuild the final PDF after DOI insertion.

## Do Not Do Before DOI Minting

- Do not invent a DOI.
- Do not hardcode a placeholder DOI in the manuscript.
- Do not cite an unfrozen artifact snapshot as the final archival version.

## After DOI Is Minted

- Insert the DOI where the manuscript cites the archival artifact.
- Re-check consistency between the manuscript, `CITATION.cff`, and `.zenodo.json`.
- Regenerate the final PDF and perform a final citation/metadata sanity check.
