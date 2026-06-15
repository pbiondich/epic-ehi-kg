# CHILD_NOTE_INFO

> The CHILD_NOTE_INFO table contains information about child notes that are linked to clinical notes. Each row represents one child note and contains information such as the user that created the link, when the link was created, and what type of link it is.

**Primary key:** `NOTE_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `NOTE_ID` | VARCHAR | PK shared | The unique identifier for the note record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TEXT_NOTE_CSN_ID` | NUMERIC |  | This holds the note contact serial number (CSN) pointer to the record where the child note's text can be found. Any workflow that links a child note to a clinical note must populate this item with the pointer to the child note contact. |
| 4 | `LINK_TYPE_C_NAME` | VARCHAR |  | This holds the type of linked note. Any workflow that links a child note to a clinical note must populate this item with the type of child note that is being linked. Different link types will have different effects on how the parent clinical note displays or behaves. |
| 5 | `LINK_USER_ID` | VARCHAR |  | Contains the user ID of the user who added the corresponding child note. Any workflow that links a child note to a clinical note must specify the user adding the link in this item. |
| 6 | `LINK_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `LINK_UTC` | DATETIME (UTC) |  | Holds the instant, in UTC format, that the child note was added to the note. Any workflow that links a child note to a clinical note must populate this item with the UTC timestamp of when the link was added. |
| 8 | `SOURCE_NOTE_CSN_ID` | NUMERIC |  | Contains the note contact serial number (CSN) of the source contact the child note was originally added to. Any workflow that links a child note to a clinical note must specify which contact on the parent clinical note the child note applies to. |
| 9 | `LINK_DTTM` | DATETIME (Local) |  | Holds the instant, in local time zone format, that the child note was added to the note. This item is automatically calculated based on the Child Note - Instant (UTC) item (I HNO 34253). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

