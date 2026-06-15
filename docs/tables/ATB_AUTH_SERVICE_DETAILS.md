# ATB_AUTH_SERVICE_DETAILS

> This table contains information about the service being requested for authorization.

**Primary key:** `AUTH_BUNDLE_ID`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `AUTH_BUNDLE_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the Auth Bundle record. |
| 2 | `AUTH_SVC_CODE_REP_C_NAME` | VARCHAR |  | The Service Code Representation category ID for the Auth Bundle.This item outlines what the "code" is that this Service represents. A code could be a recognized code set, a list or range of those code set values, or a free text string. |
| 3 | `AUTH_CODE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 4 | `AUTH_REV_CODE_ID` | NUMERIC |  | The unique ID of the Revenue Code that details the care that this particular service outlines. |
| 5 | `AUTH_REV_CODE_ID_REVENUE_CODE_NAME` | VARCHAR |  | The name of the revenue code. |
| 6 | `AUTH_MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 7 | `AUTH_PA_AMT_QUANTITY_TYPE_C_NAME` | VARCHAR |  | The Quantity Type category ID for the Auth Bundle's count information. |
| 8 | `AUTH_QUANTITY` | INTEGER |  | The Quantity amount for the Auth Bundle's count information. |
| 9 | `AUTH_PA_AMT_FREQUENCY_TYPE_C_NAME` | VARCHAR |  | The Frequency Type category ID for the Auth Bundle's count information. |
| 10 | `AUTH_FREQUENCY` | INTEGER |  | The Frequency amount for the Auth Bundle's count information. |
| 11 | `AUTH_PA_AMT_PERIOD_TYPE_C_NAME` | VARCHAR |  | The Period Type category ID for the Auth Bundle's count information. |
| 12 | `AUTH_PERIODS` | INTEGER |  | The Periods amount for the Auth Bundle's count information. |
| 13 | `AUTH_BED_DAY_TYPE_ID` | NUMERIC |  | The unique ID of the Bed Day for Auth Bundle services that pertain to Bed Days. |
| 14 | `AUTH_BED_DAY_TYPE_ID_BED_DAY_TYPE_NAME` | VARCHAR |  | The name of the bed day type record (i.e. ICU or non-authorized.) |
| 15 | `AUTH_BED_DAY_COUNT` | INTEGER |  | The count of days that this service represents, if this service pertains to Bed Days. |
| 16 | `AUTH_NIGHT_COUNT` | INTEGER |  | The count of nights that this service represents, if this service pertains to Bed Days. |
| 17 | `AUTH_QUANTITY_PER_PERIOD` | INTEGER |  | The Quantity Per Period amount for the Auth Bundle's count information. |
| 18 | `AUTH_PROC_CODE_DESC` | VARCHAR |  | The procedure code description storing additional information related to the procedure code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

