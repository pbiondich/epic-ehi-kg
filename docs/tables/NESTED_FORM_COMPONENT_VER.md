# NESTED_FORM_COMPONENT_VER

> This table contains information about the nested form components used in hemodynamic data entry templates and vascular ultrasound vessel tables. These include sets, subsets, fields, and field components. This table contains the information about components that can change overtime and is specific to a version of the template.

**Primary key:** `FORM_COMP_ID`, `CONTACT_DATE_REAL`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FORM_COMP_ID_NESTCOMP_NAME` | VARCHAR |  | The record name for the component. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `DISP_NAM` | VARCHAR |  | Name of the component that is displayed to end-users. |
| 4 | `COMPONENT_ACTIVE_YN` | VARCHAR |  | Whether or not this component is active |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

