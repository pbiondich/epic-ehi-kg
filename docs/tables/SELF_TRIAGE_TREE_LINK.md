# SELF_TRIAGE_TREE_LINK

> This table holds links to Self-Triage decision trees that have been sent to patients or their proxies.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `LINK_FORM_ID` | VARCHAR |  | This item holds the Self-Triage decision tree (LQF) ID of the tree that was linked to when a Self-Triage tree link was generated. |
| 4 | `LINK_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 5 | `LINK_SEND_UTC_DTTM` | DATETIME (UTC) |  | This item holds the UTC instant when a Self-Triage tree link was sent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

