# REI_HIDDEN_MEDS

> This table lists the medications that have been hidden in the Stimulation Summary activity for a particular cycle and patient.

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the cycle record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HIDDEN_MED_PAT_ID` | VARCHAR | FK→ | Stores the patient record ID of the patient whose medication is hidden (Multiple patients can be linked to a single cycle record). |
| 4 | `HIDDEN_MED_PRBLM_LIST_ID` | NUMERIC |  | Stores the ID for the simple generic form of the hidden medication. |
| 5 | `HIDDEN_MED_DISP_QTYUNIT_C_NAME` | VARCHAR | org | Stores the units of the hidden medication. |
| 6 | `HIDDEN_MED_FREQ_ID` | VARCHAR |  | Stores the frequency ID of the hidden medication. |
| 7 | `HIDDEN_MED_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 8 | `HIDDEN_MED_ROUTE_C_NAME` | VARCHAR | org | Stores the route of the hidden medication. |
| 9 | `HIDDEN_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |
| `HIDDEN_MED_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

