# BEN_ACCUMULATION_HX_ACCT

> This table contains a history of claims, charges, and manual adjustments made to account-level benefit buckets on coverages.

**Primary key:** `COVERAGE_ID`, `LINE`  
**Columns:** 49  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COVERAGE_ID` | NUMERIC | PK FK→ | The coverage record's ID. |
| 2 | `LINE` | INTEGER | PK | The line count for the coverage record's account bucket history. |
| 3 | `ACCT_BKT_PAT_ID` | VARCHAR | FK→ | The unique ID of the patient for the coverage's account bucket history. |
| 4 | `ACCT_BKT_DATE` | DATETIME |  | The date of service for the account level bucket update. |
| 5 | `ACCT_BKT_SRC_C_NAME` | VARCHAR |  | The source of the account-level bucket update. |
| 6 | `ACCT_BKT_CLAIM_ID` | NUMERIC |  | If the source of this accumulation is a claim, then this field will store the unique identifier of that accounts payable claim record. |
| 7 | `ACCT_BKT_AMT` | NUMERIC |  | The amount by which the account level bucket was adjusted. |
| 8 | `ACCT_BKT_CVG_ID` | NUMERIC |  | If this account level update is due to carryover from another coverage, this item will store the unique coverage ID of the source. |
| 9 | `ACCT_BKT_CMT` | VARCHAR |  | The free text comment about the account level bucket update. |
| 10 | `ACCT_BKT_USER_ID` | VARCHAR |  | The unique ID of the user associated with the account level bucket update. |
| 11 | `ACCT_BKT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 12 | `ACCT_BKT_ETR_ID` | NUMERIC |  | If the source was a claim, this field will store the procedure that updated the account level bucket. |
| 13 | `ACCT_IN_OUT_C` | VARCHAR |  | Stores in/out of network category ID for the bucket update, as calculated by the system. |
| 14 | `ACCT_IN_OUT_OVRD_C` | VARCHAR |  | Stores in/out of network category ID for the bucket update, if the system-calculated value was overridden. |
| 15 | `ACCT_BKT_HB_CHRG_ID` | NUMERIC |  | If an accumulation amount was due to Hospital Billing, this column stores the transaction ID that caused the accumulation. |
| 16 | `ACCT_BKT_BKT_ID` | NUMERIC |  | The ID of the coverage's account level bucket. |
| 17 | `ACCT_BKT_BKT_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 18 | `ACCT_BKT_CHARGE_ID` | NUMERIC |  | If the source is a charge, then this field will have the unique ID of the charge (ETR). Hospital Billing charges (HTR) and AP claim transactions (ETR) are not stored in this column. |
| 19 | `ACCT_BKT_INSTANT` | DATETIME (UTC) |  | Contains the instant at which this account bucket update was made. |
| 20 | `ACCT_BKT_Q4_FLAG` | VARCHAR | org | A Y/N flag to indicate whether or not fourth quarter carryover was performed for this bucket line. |
| 21 | `ACCT_BKT_Q4_FROM_LN` | INTEGER |  | The line number of the bucket that fourth quarter accumulations were carried from. |
| 22 | `ACCT_BKT_Q4_RLPD_YR` | INTEGER |  | Stores the roll period year of the bucket the current row corresponds to, if this bucket was carried to or from due to fourth quarter carryover. |
| 23 | `ACCT_BKT_ORG_SVC_DT` | DATETIME |  | The original service date for the account level bucket update. This will only be different from ACCT_BKT_DATE if the bucket update was the result of carryover. |
| 24 | `ACCT_BKT_Q4_CAND` | VARCHAR | org | This column stores a Y/N flag. It will only be Y if the bucket is configured for fourth quarter carryover and the service date was in the last quarter of the year, but fourth quarter carryover was not performed because the member was not effective on the target bucket date. |
| 25 | `ACCT_BKT_Q4_CVG_YN` | VARCHAR |  | Stores a Y/N flag that indicates whether or not this bucket update was carried from another coverage by fourth quarter carryover rule. The ID of the source coverage is stored in column ACCT_BKT_CVG_ID. |
| 26 | `ACCT_BKT_IDNT` | VARCHAR |  | The user-entered identifier for a manual account bucket entry. This is a free text field that could include a value that references an ID number, such as a claim or user ID. |
| 27 | `ACCT_BKT_EDIT_TYP_C_NAME` | VARCHAR | org | The edit type category ID for the account level bucket on a coverage. |
| 28 | `ACCT_BKT_ENTRY_TTL` | NUMERIC |  | Contains the total amount in the bucket before this update. This column is only populated for rows corresponding to manual adjustments. |
| 29 | `ACCT_BKT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 30 | `ACCT_BKT_VEN_ID_VENDOR_NAME` | VARCHAR |  | The name of the vendor. |
| 31 | `ACCT_BKT_ADMSN_DATE` | DATETIME |  | Benefit buckets that use an admission roll period use the admission start and discharge dates from the claim to determine the roll period. Each individual accumulation stores these dates from the claim. This column stores the admission date that accumulated this particular amount to the bucket. |
| 32 | `ACCT_BKT_DISCHRG_DATE` | DATETIME |  | Benefit buckets that use an admission roll period use the admission start and discharge dates from the claim to determine the roll period. Each individual accumulation stores these dates from the claim. This column stores the discharge date that accumulated this particular amount to the bucket. |
| 33 | `ACCT_BKT_EXCLCAROV_YN` | VARCHAR |  | Stores a Y/N flag indicating whether or not this account level accumulation was excluded from carryover to other coverages. Y means this accumulation was not carried over to other coverages. N or NULL means this accumulation was not excluded from carryover. |
| 34 | `ACCT_BKT_CRYOVR_ORIG_AMT` | NUMERIC |  | This column stores the original amount that we attempted to carryover to this coverage. This is only set if the original amount is different than the actual amount. |
| 35 | `ACCT_BKT_CAT_OR_ID` | VARCHAR |  | Stores the unique identifier of the record or category value used by the bucket if it is of type per extension per day. If BEN_ACCUMULATION_HX_ACCT.ACCT_BKT_ITEM is NULL, this column stores the unique identifier of a record in the INI specified by BEN_ACCUMULATION_HX_ACCT.ACCT_BKT_INI. Otherwise, this column stores the category value corresponding to the master file and item specified in those columns. If translation to community IDs (CIDs) is enabled for this deployment (e.g. in an IntraConnect setting), this column will store the category or record CID. |
| 36 | `ACCT_BKT_INI` | VARCHAR |  | Stores the INI of the master file networked to by the bucket if it is of type per extension per day. |
| 37 | `ACCT_BKT_ITEM` | INTEGER |  | Stores the item number networked to by the bucket if it is of type per extension per day and counts against categories. |
| 38 | `ACCT_BKT_COMBINED_START_DATE` | DATETIME |  | Stores the combined start date used if the bucket is of type per extension per day and is using an extension to combine accumulations from two contiguous days to determine whether a bucket exceeds the limit. |
| 39 | `ACCT_BKT_ACCUM_ID` | VARCHAR |  | Unique identifier for a single bucket accumulation. This is a machine generated value and cannot be edited. The ID is made up of three pieces: The coverage ID, the accumulation line number, and 1180. If this accumulation is carried through fourth quarter carryover a Q will be appended. |
| 40 | `ACCT_BKT_ORG_CVG_ID` | NUMERIC |  | If the account-level accumulation was carried over from another coverage, then this column contains the accumulation's original source coverage ID. Otherwise, this column is blank. |
| 41 | `ACCT_HRA_ACC_TYPE_C_NAME` | VARCHAR | org | The type of accumulation for the Health Reimbursement Arrangement (HRA) bucket |
| 42 | `ACCT_ROLLOVER_FROM_LINE` | INTEGER |  | The line that a rollover accumulation originated on. This will not be set when the source is Health Reimbursement Arrangement (HRA) deposit. |
| 43 | `ACCT_REVERSAL_OF_LN` | INTEGER |  | If a value is present, then this accumulation line is a reversal of the accumulation on the line number stored in this item. Note that if no value is present, then this accumulation line may or may not be a reversal of another accumulation line. |
| 44 | `ACCT_BKT_CROSS_ACCUM_BUCKET_ID` | NUMERIC |  | Indicates the source bucket if the accumulation was the result of cross-accumulation. |
| 45 | `ACCT_BKT_CROSS_ACCUM_BUCKET_ID_BUCKET_NAME` | VARCHAR |  | The name of the bucket. |
| 46 | `ACCT_BKT_RUNNING_TOTAL` | NUMERIC |  | Stores the running total of the bucket this line accumulated to. Roll periods are accounted for, so the amount returned is the current accumulation plus the total of previous accumulations to the same bucket and roll period. |
| 47 | `ACCT_BKT_TX_TOTAL_KEY` | VARCHAR |  | Stores a string that uniquely identifies the coverage, bucket, and roll period this transaction applies to. This simplifies joins to other accumulation data model components, such as V_BEN_ACCUMULATION_TOTALS. COVERAGE_ID must still be included in the join. |
| 48 | `ACCT_BKT_SEQ_NUM` | INTEGER |  | Stores a sequence number that indicates the order accumulation lines were added to the coverage. When accumulations are carried over, this number is not reset. For example, if accumulation 1 occurs on coverage A before accumulation 2 on coverage B, then carryover occurs from coverage A to B, the sequence number for accumulation 1 will still be before accumulation 2. This sequence number is not guaranteed to be dense/continuous, and may be NULL for accumulations that occurred before its implementation. |
| 49 | `ACCT_TRANS_ACCUMULATION_ID` | NUMERIC |  | If this accumulation was translated into a Benefits Builder style ACC record, then this column stores a link to that ACC record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ACCT_BKT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `COVERAGE_ID` | [COVERAGE](COVERAGE.md) | name_stem | high |

