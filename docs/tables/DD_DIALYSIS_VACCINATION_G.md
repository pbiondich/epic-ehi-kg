# DD_DIALYSIS_VACCINATION_G

> This table contains data elements submitted for CMS ESRD patient vaccination form.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 17  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `DLYS_VACCINE_TYPE_C_NAME` | VARCHAR | org | This item is used in dialysis regulatory reporting. It stores a dialysis patient's vaccination type. |
| 3 | `DLYS_VACCINE_STATUS_C_NAME` | VARCHAR | org | This item is used in dialysis regulatory reporting. It stores a dialysis patient's vaccination received status. |
| 4 | `DLYS_VACCINE_SUBTYPE_C_NAME` | VARCHAR | org | This item is used in dialysis regulatory reporting. It stores a dialysis patient's vaccination name. |
| 5 | `RECEIVED_DATE` | DATETIME |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's vaccination received date. |
| 6 | `RECEIVED_DATE_APPROX_YN` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores whether a dialysis patient's vaccination received date is approximate. |
| 7 | `ADVERSE_REACT_STATUS_C_NAME` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores whether a dialysis patient had an adverse reaction from the vaccination. |
| 8 | `ADVERSE_REACT_COMMENT` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores comments about an adverse reaction that a dialysis patient had from the vaccination. |
| 9 | `ADVERSE_REACT_FDA_REPORTED_C_NAME` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores whether a dialysis patient's vaccination adverse reaction was reported to the FDA. |
| 10 | `DLYS_HEPB_DOSE_TYPE_C_NAME` | VARCHAR | org | This item is used in dialysis regulatory reporting. It stores whether a dialysis patient's hepatitis B vaccination dose is part of a series or a booster. |
| 11 | `DLYS_VACCIN_NT_RCV_RSN_C_NAME` | VARCHAR | org | This item is used in dialysis regulatory reporting. It stores a dialysis patient's vaccination not received reason. |
| 12 | `VACCINE_NT_RCV_CMT` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's vaccination not received reason comments. |
| 13 | `OFFERED_DATE` | DATETIME |  | This item is used in dialysis regulatory reporting. It stores the date when the vaccination was offered to a dialysis patient. |
| 14 | `OFFERED_DATE_APPROX_YN` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores whether a dialysis patient's vaccination offered date is approximate. |
| 15 | `HEPB_ANTIHBS_STATUS_C_NAME` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores whether a dialysis patient received a hepatitis B antibody test. |
| 16 | `ANTIHBS_VALUE` | VARCHAR |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's hepatitis B antibodies test result value. |
| 17 | `ANTIHBS_DATE` | DATETIME |  | This item is used in dialysis regulatory reporting. It stores a dialysis patient's hepatitis B antibodies test date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

