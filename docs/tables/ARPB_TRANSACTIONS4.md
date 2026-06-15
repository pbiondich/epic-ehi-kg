# ARPB_TRANSACTIONS4

> This table contains information about professional billing transactions.

**Primary key:** `TX_ID`  
**Columns:** 17  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the transaction record. |
| 2 | `ENC_CLOSE_UTC_DTTM` | DATETIME (UTC) |  | The instant the encounter was closed |
| 3 | `IS_LATE_CHARGE_YN` | VARCHAR |  | Indicates whether the charge was posted after the visit was billed |
| 4 | `ENC_POST_LAG` | INTEGER |  | When the charge posted after the encounter closed and is sent on a claim, this is the difference in seconds between the encounter close and the post instant. Otherwise, it is not set. |
| 5 | `FIRST_CLAIM_SENT_LAG` | INTEGER |  | The number of seconds between the encounter close and the first claim sent for the charge |
| 6 | `LAST_CLAIM_SENT_LAG` | INTEGER |  | The number of seconds between the encounter close and the last claim sent for the charge |
| 7 | `OVR_IGNORE_SYS_CONTRACT_YN` | VARCHAR |  | This item is set to 1-Yes when there is a system calculated contract populated in I ETR 274, but an override action has taken place such that this reimbursement contract should be ignored. |
| 8 | `SPLIT_RELATED_HAR_TYPE_C_NAME` | VARCHAR | org | Identifies the system calculated related HAR type (I HAR 146) of the HAR that this charge will be split to. |
| 9 | `DELEGATE_BILL_SOURCE_TX_ID` | NUMERIC |  | The source Tapestry ETR that the charge is linked to. |
| 10 | `SPLIT_RELATED_HAR_RULE_ID` | VARCHAR |  | Indicates the rule in the PB Profile that qualified the charge for the related visit account type stored in item 16801. |
| 11 | `SPLIT_RELATED_HAR_RULE_ID_RULE_NAME` | VARCHAR |  | The name of the rule. |
| 12 | `OVRD_SPLIT_RELATED_HAR_TYPE_C_NAME` | VARCHAR |  | Identifies the manually overridden related HAR type (I HAR 146) of the HAR that this charge will be split to. |
| 13 | `REV_SPEC_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 14 | `REV_SUBSPEC_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 15 | `MEDICATION_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 16 | `SPLIT_RELATED_HAR_SOURCE_C_NAME` | VARCHAR |  | Tracks how the related visit account type stored in ETR item 16801/16803 was set. |
| 17 | `DELEGATE_BILL_SOURCE_CLAIM_ID` | NUMERIC |  | The source Tapestry CLM that the charge is linked to. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

