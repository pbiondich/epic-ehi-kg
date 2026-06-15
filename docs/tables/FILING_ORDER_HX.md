# FILING_ORDER_HX

> This table stores the filing order changes for a member.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the Filing Order History record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `FO_EFF_DT` | DATETIME |  | The effective date of the filing order for a coverage |
| 6 | `CVG_ID` | NUMERIC | FK→ | This item stores the coverage ID. |
| 7 | `MANUAL_FILING_ORDER` | INTEGER |  | The manual filing order of the coverage. |
| 8 | `AUTO_FILING_ORDER` | INTEGER |  | The automatic filing order of the coverage. |
| 9 | `CVG_EFF_YN` | VARCHAR |  | Flag indicating if the coverage is effective |
| 10 | `MANUAL_FO_C_NAME` | VARCHAR |  | This item stores the category of the manual filing order. |
| 11 | `AFO_ASSIGNED_TIER` | VARCHAR |  | This item stores the tier assigned to a coverage by based on the logic on the configuration table. |
| 12 | `COVERED_STATUS_C_NAME` | VARCHAR |  | This item stores the covered status of the coverage. |
| 13 | `AFO_TIEBREAKER_C_NAME` | VARCHAR | org | The tier of the Automatic Filing Order (AFO) tiebreaker that a coverage matched on."-" (category value 30) indicates that the tiebreaker was calculated, but not present. An empty value means that the filing order history contact was saved before the system started saving the tiebreaker. |
| 14 | `AFO_TIEBREAKER_SORT_C_NAME` | VARCHAR | org | The sort order for coverages that match on the same tiebreaker line (AFO_TIEBREAKER_C). "-" (category value 30) represents that the tiebreaker sort order was calculated, but not present. An empty value means that the filing order history contact was saved before the system started saving the tiebreaker sort order. |
| 15 | `GROUP_NUMBER` | VARCHAR |  | This column stores what the group number was for this coverage during the filing order effective range. Group number is an identification number assigned to the employer or plan group. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

