# HH_PAT_INSTRUCTION

> Contains user entries on the Home Health Patient Instructions form.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONTACT_DATE_REAL` | FLOAT |  | Unique identifier for this contact for this patient. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `INSTRUCTION_TPC_C_NAME` | VARCHAR | org | Instruction topic category list selections. Links to category table ZC_INSTRUCTION_TPC. |
| 4 | `INSTR_RECV_C_NAME` | VARCHAR | org | "Instructions received by" category list selections. Links to category table ZC_INSTR_RECV. |
| 5 | `INSTR_EVAL_C_NAME` | VARCHAR | org | Instruction evaluation category list selections. Links to category table ZC_INSTR_EVAL. |
| 6 | `INSTR_COMMENTS` | VARCHAR |  | Instruction comments typed in by user. |
| 7 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 8 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 9 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is populated only if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

