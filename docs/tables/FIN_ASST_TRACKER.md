# FIN_ASST_TRACKER

> This table contains information related to a financial assistance program tracker record.

**Primary key:** `FIN_ASST_TRACKER_ID`  
**Columns:** 26  
**Org-specific columns:** 6  
**Joined by:** 27 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FIN_ASST_TRACKER_ID` | NUMERIC | PK | The unique identifier for the financial assistance program tracker record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 3 | `FIN_ASST_PROGRAM_ID` | NUMERIC | FK→ | The unique ID of the financial assistance program that is associated with this tracker record. |
| 4 | `FIN_ASST_PROGRAM_ID_PROGRAM_NAME` | VARCHAR |  | The name of the financial assistance program record. |
| 5 | `FIN_ASST_CASE_ID` | NUMERIC | FK→ | This item stores the financial assistance case associated with the program tracker. |
| 6 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient associated with this tracker record. |
| 7 | `STATUS_C_NAME` | VARCHAR | org | The category ID of the status of a financial assistance program tracker record. |
| 8 | `DECISION_DATE` | DATETIME |  | Stores the decision date once the tracker has been approved or denied. The date on which a decision is taken whether to approve or deny the financial assistance program tracker. |
| 9 | `START_DATE` | DATETIME |  | The date from which this approved financial assistance program tracker is effective. |
| 10 | `END_DATE` | DATETIME |  | The date until which this approved financial assistance program tracker is effective. |
| 11 | `LETTER_SENT_STATUS_C_NAME` | VARCHAR | org | This item stores the status of an approval or denial letter sent for a tracker. |
| 12 | `APPL_RECVD_DATE` | DATETIME |  | Date the application was submitted. May or may not be the same date the application was entered as a tracker. |
| 13 | `PROGRAM_SOURCE_C_NAME` | VARCHAR | org | The source classification of the entity providing funding for the financial assistance program. |
| 14 | `PROGRAM_METHOD_C_NAME` | VARCHAR | org | The method used by the assistance program to provide financial assistance to the patient (e.g. Free drug, co-pay card). |
| 15 | `DENIAL_REASON_C_NAME` | VARCHAR | org | This item stores the reason why a financial assistance tracker is denied. |
| 16 | `APPROVAL_TYPE_C_NAME` | VARCHAR | org | This item stores the amount, type, or level of approval for a financial assistance program tracker. |
| 17 | `TOTAL_APPROVED_AMOUNT` | NUMERIC |  | The total amount of aid approved for a financial assistance program. |
| 18 | `PENDING_COVERAGE_ID` | NUMERIC |  | The unique ID of the coverage auto-created for the tracker. |
| 19 | `FOLLOW_UP_DATE` | DATETIME |  | Date on which a user should follow-up for the tracker. |
| 20 | `PRIMARY_SERV_AREA_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 21 | `DAILY_PAY_AMOUNT` | NUMERIC |  | Patient's daily pay amount for a hospital stay calculated taking their income, expenses, assets, and other financial information into consideration. |
| 22 | `WRT_OFF_LAST_UPDATE_UTC_DTTM` | DATETIME (UTC) |  | The instant that the write-off amounts for the tracker were last updated. |
| 23 | `WRT_OFF_HB_SELF_PAY_AMOUNT` | NUMERIC |  | The hospital billing self-pay amount written off as a result of approving the tracker. |
| 24 | `WRT_OFF_HB_FIN_ASST_AMOUNT` | NUMERIC |  | The hospital billing financial assistance amount written off as a result of approving the tracker. |
| 25 | `WRT_OFF_PB_SELF_PAY_AMOUNT` | NUMERIC |  | The professional billing self-pay amount written off as a result of approving the tracker. |
| 26 | `WRT_OFF_PB_FIN_ASST_AMOUNT` | NUMERIC |  | The professional billing financial assistance amount written off as a result of approving the tracker. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `FIN_ASST_CASE_ID` | [FIN_ASST_CASE](FIN_ASST_CASE.md) | sole_pk | high |
| `FIN_ASST_PROGRAM_ID` | [FIN_ASST_PROGRAM](FIN_ASST_PROGRAM.md) | sole_pk | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (27)

| From | Column | Confidence |
|------|--------|------------|
| [ARPB_TX_FIN_ASST](ARPB_TX_FIN_ASST.md) | `FIN_ASST_TRACKER_ID` | high |
| [CHG_TX_EXPECTED_WRT_OFF](CHG_TX_EXPECTED_WRT_OFF.md) | `FIN_ASST_TRACKER_ID` | high |
| [DECISION_LETTERS](DECISION_LETTERS.md) | `FIN_ASST_TRACKER_ID` | high |
| [DECISION_SERVICE_EPISODES](DECISION_SERVICE_EPISODES.md) | `FIN_ASST_TRACKER_ID` | high |
| [FA_TRACKER_SERVICE_AREAS](FA_TRACKER_SERVICE_AREAS.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_INFO](FIN_ASST_INFO.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_LETTER](FIN_ASST_LETTER.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRACKERS_FOR_LTR](FIN_ASST_TRACKERS_FOR_LTR.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRACKER_MA_MEDS](FIN_ASST_TRACKER_MA_MEDS.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_COVERAGES](FIN_ASST_TRKR_COVERAGES.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_FLAG](FIN_ASST_TRKR_FLAG.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_FLAG_UPD_HX](FIN_ASST_TRKR_FLAG_UPD_HX.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_MED_UPD_HX](FIN_ASST_TRKR_MED_UPD_HX.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_RESTR_AC_CL](FIN_ASST_TRKR_RESTR_AC_CL.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_RESTR_GUAR](FIN_ASST_TRKR_RESTR_GUAR.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_RESTR_LOC](FIN_ASST_TRKR_RESTR_LOC.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_RST_ACCL_HX](FIN_ASST_TRKR_RST_ACCL_HX.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_RST_GUAR_HX](FIN_ASST_TRKR_RST_GUAR_HX.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_RST_LOC_HX](FIN_ASST_TRKR_RST_LOC_HX.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_RTE_EVT_HX](FIN_ASST_TRKR_RTE_EVT_HX.md) | `FIN_ASST_TRACKER_ID` | high |
| [FIN_ASST_TRKR_UPDATE_HX](FIN_ASST_TRKR_UPDATE_HX.md) | `FIN_ASST_TRACKER_ID` | high |
| [HSP_ACCT_EXPECTED_WRT_OFF](HSP_ACCT_EXPECTED_WRT_OFF.md) | `FIN_ASST_TRACKER_ID` | high |
| [MPI_HX](MPI_HX.md) | `FIN_ASST_TRACKER_ID` | high |
| [MPI_ID](MPI_ID.md) | `FIN_ASST_TRACKER_ID` | high |
| [PRE_AR_CHG_3](PRE_AR_CHG_3.md) | `FIN_ASST_TRACKER_ID` | high |
| [SOCIAL_CARE_TRACKER](SOCIAL_CARE_TRACKER.md) | `FIN_ASST_TRACKER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_FNT](V_EHI_REG_ITEM_AUDIT_FNT.md) | `FIN_ASST_TRACKER_ID` | high |

