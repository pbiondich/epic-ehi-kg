# PATIENT_SA_ACCESS

> This table keeps track of the events (ADT, Cadence, Referral) that can update patient's service area.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `SA_KEY` | VARCHAR |  | Identifies a unique event that may update the patient record's service area items. The unique event may be from Admission/Discharge/Transfer information, Cadence, or Referral. |
| 6 | `SA_ACCESSED` | VARCHAR |  | Identifies service area associated with "Service area update" event in column SA_KEY. For example, if an admission event is fired for admitting patient in service area "A", then this column will contain value "A". |
| 7 | `SA_EXPR_DATE` | DATETIME |  | Identifies service area expiration date associated with service area in column SA_ACCESSED. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

