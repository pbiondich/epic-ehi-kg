# EOW_MED_ALG_INT

> This table reflects the medical data in the In Basket Messages (EOW) master file. Stores a variety of details regarding medications and allergies.

**Primary key:** `MSG_ID`, `LINE`  
**Columns:** 13  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MSG_ID` | VARCHAR | PK FK→ | The unique identifier for the task record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEDALT_ERX_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 4 | `MEDALT_TYP_C_NAME` | VARCHAR | org | Stores the Interaction details. The type of Interaction. |
| 5 | `MEDALT_DES` | VARCHAR |  | Stores the Interaction details. Interaction description. |
| 6 | `MEDALT_ELG_ID` | NUMERIC |  | Stores the Interaction details. The allergen (ELG) ID. |
| 7 | `MEDALT_ELG_ID_ALLERGEN_NAME` | VARCHAR |  | The name of the allergen record. |
| 8 | `MEDALT_LPL_ID` | NUMERIC |  | Stores the Interaction details. The allergy (LPL) ID. |
| 9 | `MEDALT_LVL_C_NAME` | VARCHAR | org | Stores the Interaction details. The Interaction level. |
| 10 | `MEDALT_OVRDRSN_C_NAME` | VARCHAR | org | Stores the Interaction details. The override reason at an individual interaction level. |
| 11 | `MEDALT_OVRDCMT` | VARCHAR |  | Stores the Interaction details. The override comment at an Individual interaction level. |
| 12 | `MEDALT_ORD_ID` | NUMERIC |  | Stores the Interaction details. The interaction medications order ID. |
| 13 | `INACT_INGRED_C_NAME` | VARCHAR |  | It indicates the inactive ingredient drug-allergy status. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MSG_ID` | [IB_MESSAGES](IB_MESSAGES.md) | sole_pk | high |

