# MLSIG_LEVEL_2

> This table is for specific sig lines of multiline sigs.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 25  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MLSIG_LINK_TO_LVL1` | INTEGER |  | The set of medication instructions this row corresponds with, for a medication which has multiple sets of dosage instructions for specified periods of time. Together with ORDER_ID, this forms the foreign key to the MLSIG_LEVEL_1 table. |
| 4 | `MLSIG_FREQ_ID` | VARCHAR |  | The unique identifier for the frequency record associated with the medication instructions for a specific period of time, indicating when and how often the medication should be administered. |
| 5 | `MLSIG_FREQ_ID_FREQ_NAME` | VARCHAR |  | The name of the frequency record. |
| 6 | `MLSIG_ORD_DOSE` | VARCHAR |  | The dose amount that was ordered for the medication, as part of the medication instructions for a specific period of time. |
| 7 | `MLSIG_ORD_DS_UNIT_C_NAME` | VARCHAR | org | The med & dose units category ID for the order record, associated with the dose amount that was ordered for a specific period of time. |
| 8 | `MLSIG_UNRND_DOSE` | VARCHAR |  | The unrounded dose amount for the medication, as part of the medication instructions for a specific period of time. |
| 9 | `MLSIG_UNRND_DS_U_C_NAME` | VARCHAR |  | The med & dose units category ID for the order record, associated with the unrounded dose amount for a specific period of time. |
| 10 | `MLSIG_CALCD_DOSE` | VARCHAR |  | The calculated dose amount for the medication, as part of the medication instructions for a specific period of time. |
| 11 | `MLSIG_CALCD_DS_U_C_NAME` | VARCHAR |  | The med & dose units category ID for the order record, associated with the calculated dose amount for a specific period of time. |
| 12 | `MLSIG_ADMIN_DOSE` | VARCHAR |  | The dose amount to be administered for the medication, as part of the medication instructions for a specific period of time. |
| 13 | `MLSIG_ADMIN_DS_U_C_NAME` | VARCHAR |  | The med & dose units category ID for the order record, associated with the dose amount to be administered for a specific period of time. |
| 14 | `MLSIG_DOSE_CALCN` | VARCHAR |  | The calculations for the medication dosage for a specific period of time. |
| 15 | `MLSIG_DS_CALCN_WARN` | VARCHAR |  | Warnings about the dose calculation for the medication dosage for a specific period of time. |
| 16 | `MLSIG_ADJUSTMENT_TYPE_C_NAME` | VARCHAR |  | The dose adjustment type category ID for the medication instructions in an order record. |
| 17 | `MLSIG_ADJUSTMENT_OVERRIDE_YN` | VARCHAR |  | Indicates whether a dose adjustment or limit was overridden for the medication instructions in the order record. 'Y' indicates that a dose adjustment or limit was overridden. 'N' or NULL indicate that a dose adjustment or limit was not overridden. |
| 18 | `MLSIG_ADJUSTMENT_ACCEPTED_YN` | VARCHAR |  | Indicates whether a dose adjustment or limit was accepted for the medication instructions in the order record. 'Y' indicates that a dose adjustment or limit was accepted. 'N' or NULL indicate that a dose adjustment or limit was not accepted. |
| 19 | `MLSIG_RND_ACK_RSN_C_NAME` | VARCHAR | org | The reason for action category ID for the order record, indication the reason selected when a user acknowledged a warning about rounding the medication dose. |
| 20 | `MLSIG_DOSE_LIMTYP_C_NAME` | VARCHAR |  | The dose adjustment type category ID for an order record, representing the type of dosage limit for a medication. |
| 21 | `MLSIG_SCHED_FIRST_DOSE_DTTM` | DATETIME (Local) |  | Stores the date and time that the first dose in an admission should be scheduled for an individual part of a multiline sig order. |
| 22 | `MLSIG_SCHED_LAST_DOSE_DTTM` | DATETIME (Local) |  | Stores the date and time that the las dose in an admission should be scheduled for an individual part of a multiline sig |
| 23 | `MLSIG_NUMBER_OF_DOSES` | INTEGER |  | Stores the number of doses for a multiline sig part (when scheduled) |
| 24 | `MLSIG_EXACT_TM` | DATETIME (Local) |  | Stores the exact time for the dosage specified in an individual part of a multiline sig |
| 25 | `MLSIG_PRN_FLAG_YN` | VARCHAR |  | This item stores PRN flag of the multiline sig dosage part. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

