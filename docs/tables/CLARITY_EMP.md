# CLARITY_EMP

> This table contains high-level information about user records from the User master file.

**Primary key:** `USER_ID`  
**Columns:** 3  
**Joined by:** 88 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `USER_ID` | VARCHAR | PK | The unique ID assigned to the user record. This ID may be encrypted. |
| 2 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 3 | `NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (88)

| From | Column | Confidence |
|------|--------|------------|
| [ABN_NOTES](ABN_NOTES.md) | `USER_ID` | high |
| [ACCOUNT_CONTACT](ACCOUNT_CONTACT.md) | `USER_ID` | high |
| [AGENDA_HX_NET_EMP_USERS](AGENDA_HX_NET_EMP_USERS.md) | `USER_ID` | high |
| [AI_INTRCT_INFO](AI_INTRCT_INFO.md) | `USER_ID` | high |
| [ALT_HISTORY](ALT_HISTORY.md) | `USER_ID` | high |
| [ARPB_TRANSACTIONS](ARPB_TRANSACTIONS.md) | `USER_ID` | high |
| [ARPB_TX_RETRO_HX](ARPB_TX_RETRO_HX.md) | `USER_ID` | high |
| [CAL_COMM_TRACKING](CAL_COMM_TRACKING.md) | `USER_ID` | high |
| [CAP_PAYMENT](CAP_PAYMENT.md) | `USER_ID` | high |
| [CAP_PAY_REPL](CAP_PAY_REPL.md) | `USER_ID` | high |
| [CAP_RR](CAP_RR.md) | `USER_ID` | high |
| [CASE_EVENT](CASE_EVENT.md) | `USER_ID` | high |
| [CELL_THERAPY_REQ_VERIFY](CELL_THERAPY_REQ_VERIFY.md) | `USER_ID` | high |
| [CHAT_PARTICIPANT](CHAT_PARTICIPANT.md) | `USER_ID` | high |
| [CLAIM_INFO](CLAIM_INFO.md) | `USER_ID` | high |
| [CLARITY_ADT](CLARITY_ADT.md) | `USER_ID` | high |
| [COMMISSION_PAYMENT](COMMISSION_PAYMENT.md) | `USER_ID` | high |
| [COMM_TRACE_EMAIL_RECPNTS](COMM_TRACE_EMAIL_RECPNTS.md) | `USER_ID` | high |
| [DEMOG_AUTH_AUDIT](DEMOG_AUTH_AUDIT.md) | `USER_ID` | high |
| [DETAIL_BILL_HX](DETAIL_BILL_HX.md) | `USER_ID` | high |
| [DIFFERENCE_PERIOD_EVENT](DIFFERENCE_PERIOD_EVENT.md) | `USER_ID` | high |
| [ED_DISPO_AUDIT](ED_DISPO_AUDIT.md) | `USER_ID` | high |
| [ED_FOLLOWUP_AUDIT](ED_FOLLOWUP_AUDIT.md) | `USER_ID` | high |
| [ESC_RESPONSIBLE_USERS](ESC_RESPONSIBLE_USERS.md) | `USER_ID` | high |
| [HEALTH_CARE_AGENT_HX](HEALTH_CARE_AGENT_HX.md) | `USER_ID` | high |
| [HH_CPLN_ENC](HH_CPLN_ENC.md) | `USER_ID` | high |
| [HH_MED_ORD_POC_STATUS](HH_MED_ORD_POC_STATUS.md) | `USER_ID` | high |
| [HH_PROB_ENC](HH_PROB_ENC.md) | `USER_ID` | high |
| [HSP_ACCT_CONS_SP_STS_HX](HSP_ACCT_CONS_SP_STS_HX.md) | `USER_ID` | high |
| [HSP_BFH_ACTIVITY](HSP_BFH_ACTIVITY.md) | `USER_ID` | high |
| [HSP_PRE_AR_BND_EPSD_HX](HSP_PRE_AR_BND_EPSD_HX.md) | `USER_ID` | high |
| [HSP_TRANSACTIONS](HSP_TRANSACTIONS.md) | `USER_ID` | high |
| [LETTER_PRINT_AUDIT](LETTER_PRINT_AUDIT.md) | `USER_ID` | high |
| [MAR_ADMIN_EDITD](MAR_ADMIN_EDITD.md) | `USER_ID` | high |
| [MAR_ADMIN_INFO](MAR_ADMIN_INFO.md) | `USER_ID` | high |
| [MYC_CONVO_USERS](MYC_CONVO_USERS.md) | `USER_ID` | high |
| [MYC_LETTER_RELEASE](MYC_LETTER_RELEASE.md) | `USER_ID` | high |
| [NOTE_SMARTBLOCK_ATTR](NOTE_SMARTBLOCK_ATTR.md) | `USER_ID` | high |
| [OCS_CODE_STATUS](OCS_CODE_STATUS.md) | `USER_ID` | high |
| [ORDER_HOLD_INFO](ORDER_HOLD_INFO.md) | `USER_ID` | high |
| [ORDER_PENDING](ORDER_PENDING.md) | `USER_ID` | high |
| [ORDER_RAD_AUDIT](ORDER_RAD_AUDIT.md) | `USER_ID` | high |
| [ORDER_RAD_STUDY](ORDER_RAD_STUDY.md) | `USER_ID` | high |
| [ORD_OPIMS_OVERRIDE](ORD_OPIMS_OVERRIDE.md) | `USER_ID` | high |
| [OTP_OPIMS_OVERRIDE](OTP_OPIMS_OVERRIDE.md) | `USER_ID` | high |
| [PATIENT_NOTICE](PATIENT_NOTICE.md) | `USER_ID` | high |
| [PAT_CARE_REG](PAT_CARE_REG.md) | `USER_ID` | high |
| [PAT_LIFEDOSE_HX](PAT_LIFEDOSE_HX.md) | `USER_ID` | high |
| [PAT_SVC_PROV_SEARCH_ACT](PAT_SVC_PROV_SEARCH_ACT.md) | `USER_ID` | high |
| [PAT_SVC_PROV_SEARCH_LIST](PAT_SVC_PROV_SEARCH_LIST.md) | `USER_ID` | high |
| [PRE_AR_CHG_HX](PRE_AR_CHG_HX.md) | `USER_ID` | high |
| [PROB_CONTACT](PROB_CONTACT.md) | `USER_ID` | high |
| [PR_EST_INFO](PR_EST_INFO.md) | `USER_ID` | high |
| [PT_GOALS_INFO](PT_GOALS_INFO.md) | `USER_ID` | high |
| [REFERRAL_APT](REFERRAL_APT.md) | `USER_ID` | high |
| [REIMB_CALC_HX](REIMB_CALC_HX.md) | `USER_ID` | high |
| [RFL_VOIDED_NOTES](RFL_VOIDED_NOTES.md) | `USER_ID` | high |
| [RXA_ATTEMPT](RXA_ATTEMPT.md) | `USER_ID` | high |
| [RX_IVENT_USERINFO](RX_IVENT_USERINFO.md) | `USER_ID` | high |
| [SPEC_CHG_TRGR_TRACE](SPEC_CHG_TRGR_TRACE.md) | `USER_ID` | high |
| [TOPIC_HX_NET_EMP_USERS](TOPIC_HX_NET_EMP_USERS.md) | `USER_ID` | high |
| [VARIANCE](VARIANCE.md) | `USER_ID` | high |
| [V_EHI_AUDIT_BEN](V_EHI_AUDIT_BEN.md) | `USER_ID` | high |
| [V_EHI_AUDIT_CLM](V_EHI_AUDIT_CLM.md) | `USER_ID` | high |
| [V_EHI_AUDIT_CVG](V_EHI_AUDIT_CVG.md) | `USER_ID` | high |
| [V_EHI_AUDIT_CVG_MEM_1](V_EHI_AUDIT_CVG_MEM_1.md) | `USER_ID` | high |
| [V_EHI_AUDIT_CVG_MEM_2](V_EHI_AUDIT_CVG_MEM_2.md) | `USER_ID` | high |
| [V_EHI_AUDIT_CVG_MEM_3](V_EHI_AUDIT_CVG_MEM_3.md) | `USER_ID` | high |
| [V_EHI_AUDIT_CVG_SUBS](V_EHI_AUDIT_CVG_SUBS.md) | `USER_ID` | high |
| [V_EHI_AUDIT_DCS](V_EHI_AUDIT_DCS.md) | `USER_ID` | high |
| [V_EHI_AUDIT_EAR](V_EHI_AUDIT_EAR.md) | `USER_ID` | high |
| [V_EHI_AUDIT_EPT](V_EHI_AUDIT_EPT.md) | `USER_ID` | high |
| [V_EHI_AUDIT_EPT_ENC](V_EHI_AUDIT_EPT_ENC.md) | `USER_ID` | high |
| [V_EHI_AUDIT_HAR](V_EHI_AUDIT_HAR.md) | `USER_ID` | high |
| [V_EHI_AUDIT_OYO](V_EHI_AUDIT_OYO.md) | `USER_ID` | high |
| [V_EHI_AUDIT_RLA](V_EHI_AUDIT_RLA.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_BEN](V_EHI_REG_ITEM_AUDIT_BEN.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_CLM](V_EHI_REG_ITEM_AUDIT_CLM.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_CVG](V_EHI_REG_ITEM_AUDIT_CVG.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_EAR](V_EHI_REG_ITEM_AUDIT_EAR.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_EPT](V_EHI_REG_ITEM_AUDIT_EPT.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_FNC](V_EHI_REG_ITEM_AUDIT_FNC.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_FNT](V_EHI_REG_ITEM_AUDIT_FNT.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_HAR](V_EHI_REG_ITEM_AUDIT_HAR.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_OYO](V_EHI_REG_ITEM_AUDIT_OYO.md) | `USER_ID` | high |
| [V_EHI_REG_ITEM_AUDIT_RLA](V_EHI_REG_ITEM_AUDIT_RLA.md) | `USER_ID` | high |
| [WOUND_THERAPY_TREATMENTS](WOUND_THERAPY_TREATMENTS.md) | `USER_ID` | high |
| [WOUND_THERAPY_TREAT_AUDIT](WOUND_THERAPY_TREAT_AUDIT.md) | `USER_ID` | high |

