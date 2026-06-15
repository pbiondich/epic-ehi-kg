# INV_TEMPLATE_INFO

> Clarity table to extract information about intervention templates.

**Primary key:** `INTERVENTION_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INTERVENTION_ID` | VARCHAR | PK FK→ | The unique identifier for the intervention record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TASK_TEMPLATES_ID` | VARCHAR |  | Task template ID for the intervention record. |
| 4 | `TASK_TEMPLATES_ID_RECORD_NAME` | VARCHAR |  | This column displays the name of the task template record. |
| 5 | `TASK_TEMPLATES_DAT` | NUMERIC |  | Intervention task template contact used. |
| 6 | `LPI_LTI_ID` | NUMERIC |  | The source intervention template id of the patient intervention record. |
| 7 | `LPI_LTI_ID_INTERVENTION_NAME` | VARCHAR |  | This column displays the intervention name. |
| 8 | `LPI_LTI_DAT` | NUMERIC |  | Source intervention template DAT for the patient intervention record. |
| 9 | `INVTMPL_MERGE_DAT` | NUMERIC |  | Contact where the template is created/merged. |
| 10 | `DUP_ACT_APPLIED_C_NAME` | VARCHAR |  | Duplicate action used to create/merge the template. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `INTERVENTION_ID` | [INTERVENTION](INTERVENTION.md) | name_stem | high |

