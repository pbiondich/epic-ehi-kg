# EVENT

> The EVENT table contains high-level information about events.

**Primary key:** `EVENT_ID`  
**Columns:** 2  
**Joined by:** 25 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK | The unique ID of the event. |
| 2 | `EVENT_NAME` | VARCHAR |  | The name of the event. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (25)

| From | Column | Confidence |
|------|--------|------------|
| [ADT_SPLIT_ACCT_INTERP_HX](ADT_SPLIT_ACCT_INTERP_HX.md) | `EVENT_ID` | high |
| [CLARITY_ADT](CLARITY_ADT.md) | `EVENT_ID` | high |
| [ED_EVENT_HISTORY](ED_EVENT_HISTORY.md) | `EVENT_ID` | high |
| [ED_IEV_EVENT_INFO](ED_IEV_EVENT_INFO.md) | `EVENT_ID` | high |
| [ED_IEV_EVENT_INFO_FLAGS](ED_IEV_EVENT_INFO_FLAGS.md) | `EVENT_ID` | high |
| [ED_IEV_LINKED_ORDER_INFO](ED_IEV_LINKED_ORDER_INFO.md) | `EVENT_ID` | high |
| [ED_IEV_PAT_INFO](ED_IEV_PAT_INFO.md) | `EVENT_ID` | high |
| [EVENT_NOTIF_HX](EVENT_NOTIF_HX.md) | `EVENT_ID` | high |
| [EVENT_USER_ACTIONS](EVENT_USER_ACTIONS.md) | `EVENT_ID` | high |
| [FLAG_FOR_REMOVAL_CRITERIA](FLAG_FOR_REMOVAL_CRITERIA.md) | `EVENT_ID` | high |
| [HOME_MEDS_REORDERS](HOME_MEDS_REORDERS.md) | `EVENT_ID` | high |
| [IP_ORDER_REC](IP_ORDER_REC.md) | `EVENT_ID` | high |
| [IP_PEND_MED_REC](IP_PEND_MED_REC.md) | `EVENT_ID` | high |
| [IP_POST_MED_REC_ORDERS](IP_POST_MED_REC_ORDERS.md) | `EVENT_ID` | high |
| [IP_SNAPSHOT_SUM](IP_SNAPSHOT_SUM.md) | `EVENT_ID` | high |
| [LOA_UPDATES](LOA_UPDATES.md) | `EVENT_ID` | high |
| [MED_REC_DOSE_COPIED_FROM](MED_REC_DOSE_COPIED_FROM.md) | `EVENT_ID` | high |
| [PEND_RESUME_IOU_RM](PEND_RESUME_IOU_RM.md) | `EVENT_ID` | high |
| [PND_REC_DOSE_COPIED_FROM](PND_REC_DOSE_COPIED_FROM.md) | `EVENT_ID` | high |
| [REACTIVATED_EXP_ORDERS](REACTIVATED_EXP_ORDERS.md) | `EVENT_ID` | high |
| [REFERRAL_NOTIF_HIS](REFERRAL_NOTIF_HIS.md) | `EVENT_ID` | high |
| [SNAPSHOT_ORDERS](SNAPSHOT_ORDERS.md) | `EVENT_ID` | high |
| [SNAPSHOT_ORDER_DATA](SNAPSHOT_ORDER_DATA.md) | `EVENT_ID` | high |
| [SNAPSHOT_ORD_INFO_VALUE](SNAPSHOT_ORD_INFO_VALUE.md) | `EVENT_ID` | high |
| [TX_DAY_REC](TX_DAY_REC.md) | `EVENT_ID` | high |

