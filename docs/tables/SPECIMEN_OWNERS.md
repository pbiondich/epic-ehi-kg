# SPECIMEN_OWNERS

> The owners of a fertility embryo, oocyte, or sperm. These owners have the ability to make decisions about how the specimen will be used, and the specimens will appear in the owners' cryopreservation inventory.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `OWNERS_PAT_ID` | VARCHAR | FK→ | Stores the patients who own a given embryo, oocyte, or sperm. These patients are able to decide whether the specimen can be used for reproduction. |
| 4 | `OWNERS_NONPAT_RECORD_ID` | NUMERIC |  | Stores the people or entities (non-patient records) who own a given embryo, oocyte, or sperm. They are able to decide whether the specimens can be used for reproduction. |
| 5 | `OWNER_COMMENTS` | VARCHAR |  | Comments associated with the owner of the specimen |
| 6 | `OWNERS_LAB_ID_LAB_NAME` | VARCHAR |  | The name of the lab record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OWNERS_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

