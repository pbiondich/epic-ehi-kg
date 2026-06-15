# CW_ABST_VACCINATIONS

> Vaccination information from abstractions with clinical information reported to the United States ESRD patient registry.

**Primary key:** `REGISTRY_DATA_ID`  
**Columns:** 23  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier for the registry data record. |
| 2 | `FLU_NOT_RECV_YN` | VARCHAR |  | Shows whether the dialysis patient has received influenza vaccination or not. |
| 3 | `FLU_SITE_C_NAME` | VARCHAR |  | The dialysis patient's influenza vaccination site. |
| 4 | `FLUE_DATE` | DATETIME |  | The dialysis patient's influenza vaccination date. |
| 5 | `PCV13_NOT_RECV_YN` | VARCHAR |  | Shows whether the dialysis patient has received a PCV13 pneumococcal vaccination or not. |
| 6 | `PCV13_YEAR` | INTEGER |  | The dialysis patient's PCV13 pneumococcal vaccination year. |
| 7 | `PCV13_SITE_C_NAME` | VARCHAR |  | Shows whether the dialysis patient's PCV13 pneumococcal vaccination was administered onsite or offsite. |
| 8 | `PPSV23_NOT_RECV_YN` | VARCHAR |  | Shows whether the dialysis patient has received a PPSV23 pneumococcal vaccination or not. |
| 9 | `PPSV23_YEAR` | INTEGER |  | The dialysis patient's PPSV23 pneumococcal vaccination administration year. |
| 10 | `PPSV23_SITE_C_NAME` | VARCHAR |  | Shows whether the dialysis patient's PPSV23 pneumococcal vaccination was administered onsite or offsite |
| 11 | `HEP_B_NOT_RECV_YN` | VARCHAR |  | Shows whether the dialysis patient has received hepatitis B vaccination or not. |
| 12 | `HEP_B_FIRST_DATE` | DATETIME |  | The dialysis patient's hepatitis B vaccination first dose administration date. |
| 13 | `HEP_B_SECOND_DATE` | DATETIME |  | The dialysis patient's hepatitis B vaccination second dose administration date. |
| 14 | `HEP_B_THIRD_DATE` | DATETIME |  | The dialysis patient's hepatitis B vaccination third dose administration date. |
| 15 | `HEP_B_FOURTH_DATE` | DATETIME |  | The dialysis patient's hepatitis B vaccination fourth dose administration date. |
| 16 | `HEP_B_FIRST_BOOSTER_DATE` | DATETIME |  | The dialysis patient's hepatitis B vaccination booster 1 administration date. |
| 17 | `HEP_B_SECOND_BOOSTER_DATE` | DATETIME |  | The dialysis patient's hepatitis B vaccination booster 2 administration date. |
| 18 | `HEP_B_THIRD_BOOSTER_DATE` | DATETIME |  | The dialysis patient's hepatitis B vaccination booster 3 administration date. |
| 19 | `HEP_B_FOURTH_BOOSTER_DATE` | DATETIME |  | The dialysis patient's hepatitis B vaccination booster 4 administration date. |
| 20 | `HEP_B_NOT_RECV_MED_RSN_C_NAME` | VARCHAR |  | The dialysis patient's hepatitis B vaccination not received medical reason. |
| 21 | `HEP_B_NOT_RECV_PAT_RSN_C_NAME` | VARCHAR | org | The dialysis patient's hepatitis B vaccination not received non-medical reason. |
| 22 | `HEP_B_SURFACE_ANTIBODIES_VALUE` | VARCHAR |  | The dialysis patient's hepatitis B antibodies test value. |
| 23 | `HEP_B_SURFACE_ANTIBODIES_DATE` | DATETIME |  | The dialysis patient's hepatitis B antibodies test date. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

