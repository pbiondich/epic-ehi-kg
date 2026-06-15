# REFERRAL_3

> The REFERRAL_3 table is a continuation of the REFERRAL_2 which is continuation of the REFERRAL table. These tables are the primary tables for referral information stored in the system.

**Overflow of:** [REFERRAL](REFERRAL.md)  
**Primary key:** `REFERRAL_ID`  
**Columns:** 40  
**Org-specific columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK | The unique identifier for the referral record. |
| 2 | `GEN_RFL_STR_10` | VARCHAR |  | This contains information from generic referral string item 10. |
| 3 | `GEN_RFL_CAT_11_C_NAME` | VARCHAR | org | This contains information from generic referral category item 11. |
| 4 | `GEN_RFL_CAT_12_C_NAME` | VARCHAR | org | This contains information from generic referral category item 12. |
| 5 | `GEN_RFL_CAT_13_C_NAME` | VARCHAR | org | This contains information from generic referral category item 13. |
| 6 | `GEN_RFL_CAT_14_C_NAME` | VARCHAR | org | This contains information from generic referral category item 14. |
| 7 | `GEN_RFL_CAT_15_C_NAME` | VARCHAR | org | This contains information from generic referral category item 15. |
| 8 | `REFERRING_DEP_SPC_C_NAME` | VARCHAR | org | Indicates the specialty of the department where the referral is coming from. |
| 9 | `CANCEL_RSN_C_NAME` | VARCHAR | org | Status reason explaining why a referral was canceled. |
| 10 | `PAT_COMM_DATE` | DATETIME |  | The date when the patient's scheduled encounter was communicated to the patient. |
| 11 | `GEN_RFL_CAT_16_C_NAME` | VARCHAR | org | This contains information from generic referral category item 16. |
| 12 | `GEN_RFL_CAT_17_C_NAME` | VARCHAR | org | This contains information from generic referral category item 17. |
| 13 | `GEN_RFL_CAT_18_C_NAME` | VARCHAR | org | This contains information from generic referral category item 18. |
| 14 | `GEN_RFL_CAT_19_C_NAME` | VARCHAR | org | This contains information from generic referral category item 19. |
| 15 | `GEN_RFL_CAT_20_C_NAME` | VARCHAR | org | This contains information from generic referral category item 20. |
| 16 | `GEN_RFL_CAT_21_C_NAME` | VARCHAR | org | This contains information from generic referral category item 21. |
| 17 | `GEN_RFL_CAT_22_C_NAME` | VARCHAR | org | This contains information from generic referral category item 22. |
| 18 | `GEN_RFL_CAT_23_C_NAME` | VARCHAR | org | This contains information from generic referral category item 23. |
| 19 | `GEN_RFL_CAT_24_C_NAME` | VARCHAR | org | This contains information from generic referral category item 24. |
| 20 | `GEN_RFL_CAT_25_C_NAME` | VARCHAR | org | This contains information from generic referral category item 25. |
| 21 | `GEN_RFL_STR_11` | VARCHAR |  | Referral-level generic string for general use. |
| 22 | `GEN_RFL_STR_12` | VARCHAR |  | Referral-level generic string for general use. |
| 23 | `GEN_RFL_STR_13` | VARCHAR |  | Referral-level generic string for general use. |
| 24 | `GEN_RFL_STR_14` | VARCHAR |  | Referral-level generic string for general use. |
| 25 | `GEN_RFL_STR_16` | VARCHAR |  | Referral-level generic string for general use. |
| 26 | `GEN_RFL_STR_17` | VARCHAR |  | Referral-level generic string for general use. |
| 27 | `GEN_RFL_STR_18` | VARCHAR |  | Referral-level generic string for general use. |
| 28 | `GEN_RFL_STR_19` | VARCHAR |  | Referral-level generic string for general use. |
| 29 | `GEN_RFL_STR_20` | VARCHAR |  | Referral-level generic string for general use. |
| 30 | `GEN_RFL_STR_21` | VARCHAR |  | Referral-level generic string for general use. |
| 31 | `GEN_RFL_STR_22` | VARCHAR |  | Referral-level generic string for general use. |
| 32 | `GEN_RFL_STR_23` | VARCHAR |  | Referral-level generic string for general use. |
| 33 | `GEN_RFL_STR_24` | VARCHAR |  | Referral-level generic string for general use. |
| 34 | `GEN_RFL_STR_25` | VARCHAR |  | Referral-level generic string for general use. |
| 35 | `GEN_RFL_STR_26` | VARCHAR |  | Referral-level generic string for general use. |
| 36 | `GEN_RFL_STR_27` | VARCHAR |  | Referral-level generic string for general use. |
| 37 | `GEN_RFL_STR_28` | VARCHAR |  | Referral-level generic string for general use. |
| 38 | `GEN_RFL_STR_29` | VARCHAR |  | Referral-level generic string for general use. |
| 39 | `GEN_RFL_STR_30` | VARCHAR |  | Referral-level generic string for general use. |
| 40 | `GEN_RFL_STR_15` | VARCHAR |  | Referral-level generic string for general use. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [REFERRAL](REFERRAL.md).

