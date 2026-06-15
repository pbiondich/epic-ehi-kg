# QRY_EVIDENCE

> This table extracts evidence-related information (such as vitals, medication, results) tied to a query.

**Primary key:** `QUERY_CSN_ID`, `LINE`  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `QUERY_ID` | NUMERIC | FK→ | The unique identifier for the query record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `EVIDENCE_NAME` | VARCHAR |  | The display name of the evidence. |
| 5 | `EVIDENCE_TYPE_C_NAME` | VARCHAR |  | The type of evidence used to create a query. |
| 6 | `QUERY_CSN_ID` | NUMERIC | PK FK→ | The contact serial number (CSN) of the contact. |
| 7 | `EVIDENCE_QUESTION_ID_QUEST_NAME` | VARCHAR |  | The name of the question record. |
| 8 | `EVIDENCE_COMMON_NAME` | VARCHAR |  | The common name of a lab evidence. |
| 9 | `EVIDENCE_ORDER_ID` | NUMERIC |  | The ID of the order associated with a piece of evidence. |
| 10 | `EVIDENCE_ORDER_DAT` | NUMERIC |  | The contact of the order associated with a piece of evidence. |
| 11 | `EVIDENCE_NUM_VALUE` | NUMERIC |  | The numeric value of a piece of evidence. |
| 12 | `EVIDENCE_INSTANT_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant for a piece of evidence. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `QUERY_CSN_ID` | [QRY_CONTACT_INFO](QRY_CONTACT_INFO.md) | sole_pk | high |
| `QUERY_ID` | [QRY_RECORD_INFO](QRY_RECORD_INFO.md) | sole_pk | high |

