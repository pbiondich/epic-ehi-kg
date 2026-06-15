# PAT_REL_INFO_EPSD

> This table contains episode-level relationship information about patient relationships. These relationship items are specific to certain episodes. The records included in this table are Patient Relationships (RLA) records.

**Primary key:** `PAT_RELATIONSHIP_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_RELATIONSHIP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient contact. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EPISODE_ID` | NUMERIC | FK→ | The unique ID of the episode this patient contact is linked to. |
| 4 | `EPSD_INVOLVEMENT_START_DATE` | DATETIME |  | The date when the patient contact's involvement in the episode starts. |
| 5 | `EPSD_INVOLVEMENT_END_DATE` | DATETIME |  | The date when the patient contact's involvement in the episode ends. |
| 6 | `EPSD_LAST_REV_DTTM` | DATETIME (Attached) |  | The instant that this patient contact's general or episode-specific information was last reviewed or updated. |
| 7 | `EPSD_REV_USER_ID` | VARCHAR |  | The unique ID of the last user who reviewed or updated this patient contact's information for the specific episode. |
| 8 | `EPSD_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `EPSD_DISPLAY_SEQ` | INTEGER |  | Used to save the order in which episode-level contacts for a given patient should display within a specific episode. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `PAT_RELATIONSHIP_ID` | [PAT_RELATIONSHIP_LIST](PAT_RELATIONSHIP_LIST.md) | sole_pk | high |

