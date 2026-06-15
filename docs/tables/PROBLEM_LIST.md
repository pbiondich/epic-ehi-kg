# PROBLEM_LIST

> The PROBLEM_LIST table contains data from patients' problem lists in the clinical system. The data in this table reflects the current status of all problems on the patient's problem list. In the clinical system, each problem is marked as active until it becomes (and is marked) Resolved or Deleted. At that point, by default, it will not be displayed in the application. However, any problem ever entered on this list is stored in the database and will exist in this table. Deleted and resolved problems can be viewed in the application by simply marking a checkbox to show them. Note that deleted and resolved problems can be restored by undeleting them (an option in the application). When a deleted problem is restored, its status is changed to active and the deleted date is returned to null.

**Primary key:** `PROBLEM_LIST_ID`  
**Columns:** 30  
**Org-specific columns:** 3  
**Joined by:** 68 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PROBLEM_LIST_ID` | NUMERIC | PK | The unique ID of this Problem List entry. |
| 2 | `DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 3 | `DESCRIPTION` | VARCHAR |  | The display name of the problem. Only contains data if the default display name is changed. |
| 4 | `NOTED_DATE` | DATETIME |  | Represents the first possible date that a problem could have been noted/onset on. By default, this is the problem's date of entry into the problem list. The intent of this field is to allow users to change this date to the date the problem was first diagnosed if that is different than the entry date. A problem's noted date is documented as a fuzzy date, meaning that it can capture approximate date data ("2012", "1/2012") or exact data ("3/5/2012"). This column captures the earliest date of the effective range. See NOTED_END_DATE for the latest counterpart. For example, if 2012 is documented in hyperspace, then NOTED_DATE will be 1/1/2012 and NOTED_END_DATE will be 12/31/2012. |
| 5 | `RESOLVED_DATE` | DATETIME |  | The date the problem was resolved in calendar format. |
| 6 | `DATE_OF_ENTRY` | DATETIME |  | This is the date the specific problem was last edited (i.e., a change was made, either in status, priority, etc.). |
| 7 | `ENTRY_USER_ID` | VARCHAR |  | The unique ID of the system user who last edited the problem in the patient’s Problem List. This ID may be encrypted. |
| 8 | `ENTRY_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `PROBLEM_CMT` | VARCHAR |  | The preview text (first characters) of the Overview note entered for a Problem List entry. |
| 10 | `CHRONIC_YN` | VARCHAR |  | This column indicates whether or not this problem is flagged as chronic. |
| 11 | `SHOW_IN_MYC_YN` | VARCHAR |  | Indicates whether this problem will be displayed in Epic's Patient Portal, MyChart. |
| 12 | `PROBLEM_STATUS_C_NAME` | VARCHAR |  | The category value associated with the problem’s current state: Active, Resolved, or Deleted. NOTE: Historical information regarding status changes can be viewed from within the application. |
| 13 | `CLASS_OF_PROBLEM_C_NAME` | VARCHAR | org | The category value associated with additional information for the problem, such as Acute, chronic, minor, and so on. |
| 14 | `PRIORITY_C_NAME` | VARCHAR | org | The category value associated with the relative severity of the problem. Problems can be given a priority (e.g., high, medium, or low). This field shows the category value associated with the current priority level assigned to a problem. |
| 15 | `OVERVIEW_NOTE_ID` | VARCHAR |  | This item is a link to the note record that contains the overview note pertaining to this problem record. |
| 16 | `STAGE_ID` | NUMERIC | shared | The unique ID of the cancer stage record associated with the entry in the patient’s Problem List. |
| 17 | `PROBLEM_TYPE_C_NAME` | VARCHAR |  | The problem type for this problem. |
| 18 | `CREATING_ORDER_ID` | NUMERIC |  | The order ID of the order that created the problem. |
| 19 | `NO_STAGE_REASON_C_NAME` | VARCHAR | org | For a problem that could be staged, stores the reason why it was not staged. |
| 20 | `NO_STAGE_COMMENT` | VARCHAR |  | For a problem that could be staged, stores a free-text comment explaining why the problem was not staged. |
| 21 | `NO_STAGE_USER_ID` | VARCHAR |  | For a problem that could be staged, stores the user who chose not to stage it. |
| 22 | `NO_STAGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 23 | `NO_STAGE_DTTM` | DATETIME (UTC) |  | For a problem that could be staged, stores the instant when a user flagged it to not be staged. |
| 24 | `TREAT_SUMM_STATUS_C_NAME` | VARCHAR |  | Stores the treatment summary status for this problem. |
| 25 | `NOTED_END_DATE` | DATETIME |  | Represents the last possible date that a problem could have been noted/onset on. A problem's noted date is documented as a fuzzy date, meaning that it can capture approximate date data ("2012", "1/2012") or exact data ("3/5/2012"). This column captures the latest date of the effective range. See NOTED_DATE for the earliest counterpart. For example, if 2012 is documented in hyperspace, then NOTED_DATE will be 1/1/2012 and NOTED_END_DATE will be 12/31/2012. Note that the value may be empty, even if NOTED_DATE is populated |
| 26 | `REL_GOALS_PROBLEM_LIST_CSN_ID` | NUMERIC |  | Stores the CSN (contact serial number I.E. unique contact identifier) of the last related goals contact that was edited. |
| 27 | `REL_GOALS_INST_DTTM` | DATETIME (Local) |  | Stores the instant of the last related goals contact that was edited. |
| 28 | `PROB_STAGE_STATUS_C_NAME` | VARCHAR |  | Flag to indicate whether this problem has been staged or marked as no stage required. |
| 29 | `DIAG_START_DATE` | DATETIME |  | Represents the earliest possible date that a problem could have been diagnosed on. The latest possible date is stored in DIAG_END_DATE. If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |
| 30 | `DIAG_END_DATE` | DATETIME |  | Represents the last possible date that a problem could have been diagnosed on. The earliest possible date is stored in DIAG_START_DATE. If these values are the same, then the date is exact rather than fuzzy. For a problem or condition affecting a patient, the diagnosis date is defined as the date when a qualified professional first recognized the presence of that condition with sufficient certainty, regardless of whether it was fully characterized at that time. For diseases such as cancer, this may be the earliest date of a clinical diagnosis from before it was histologically confirmed, not the date of confirmation if that occurred later. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (68)

| From | Column | Confidence |
|------|--------|------------|
| [ANTICOAG_TRTMNT_DX](ANTICOAG_TRTMNT_DX.md) | `PROBLEM_LIST_ID` | high |
| [ASSOCIATED_DX](ASSOCIATED_DX.md) | `PROBLEM_LIST_ID` | high |
| [BILIARY_LEAK_SITE](BILIARY_LEAK_SITE.md) | `PROBLEM_LIST_ID` | high |
| [CANCER_PROB_MERGE_HISTORY](CANCER_PROB_MERGE_HISTORY.md) | `PROBLEM_LIST_ID` | high |
| [COMPLICATIONS](COMPLICATIONS.md) | `PROBLEM_LIST_ID` | high |
| [COMPLICATION_DX_MODE](COMPLICATION_DX_MODE.md) | `PROBLEM_LIST_ID` | high |
| [EPI_PROBLEM_LIST](EPI_PROBLEM_LIST.md) | `PROBLEM_LIST_ID` | high |
| [HEMORRHAGE_SRC](HEMORRHAGE_SRC.md) | `PROBLEM_LIST_ID` | high |
| [HH_PBLST_HX_WND_ED](HH_PBLST_HX_WND_ED.md) | `PROBLEM_LIST_ID` | high |
| [HH_PBLST_INFO](HH_PBLST_INFO.md) | `PROBLEM_LIST_ID` | high |
| [HH_PBLST_WOUNDS](HH_PBLST_WOUNDS.md) | `PROBLEM_LIST_ID` | high |
| [IMM_COMPONENT](IMM_COMPONENT.md) | `PROBLEM_LIST_ID` | high |
| [IMM_HX_ADDTN_COMP_EXPDATE](IMM_HX_ADDTN_COMP_EXPDATE.md) | `PROBLEM_LIST_ID` | high |
| [IMM_HX_ADDTN_COMP_INV_CLS](IMM_HX_ADDTN_COMP_INV_CLS.md) | `PROBLEM_LIST_ID` | high |
| [IMM_HX_ADDTN_COMP_LOTID](IMM_HX_ADDTN_COMP_LOTID.md) | `PROBLEM_LIST_ID` | high |
| [IMM_HX_ADDTN_COMP_LOTNUM](IMM_HX_ADDTN_COMP_LOTNUM.md) | `PROBLEM_LIST_ID` | high |
| [IMM_HX_ADDTN_COMP_NDC](IMM_HX_ADDTN_COMP_NDC.md) | `PROBLEM_LIST_ID` | high |
| [IMM_HX_ADDTN_COMP_TYPE](IMM_HX_ADDTN_COMP_TYPE.md) | `PROBLEM_LIST_ID` | high |
| [INFECTION_TREAT](INFECTION_TREAT.md) | `PROBLEM_LIST_ID` | high |
| [INFECT_TREAT_HX](INFECT_TREAT_HX.md) | `PROBLEM_LIST_ID` | high |
| [LPL_RELATED_PROBS](LPL_RELATED_PROBS.md) | `PROBLEM_LIST_ID` | high |
| [LPL_VISIT_NOTES](LPL_VISIT_NOTES.md) | `PROBLEM_LIST_ID` | high |
| [MPI_LPL_ID](MPI_LPL_ID.md) | `PROBLEM_LIST_ID` | high |
| [MPI_LPL_ID_HX](MPI_LPL_ID_HX.md) | `PROBLEM_LIST_ID` | high |
| [MTP_AUTO_EVAL_DIAGNOSES](MTP_AUTO_EVAL_DIAGNOSES.md) | `PROBLEM_LIST_ID` | high |
| [ORDER_PROC](ORDER_PROC.md) | `PROBLEM_LIST_ID` | high |
| [ORGANISMS](ORGANISMS.md) | `PROBLEM_LIST_ID` | high |
| [PANCREAS_LEAK_SITE](PANCREAS_LEAK_SITE.md) | `PROBLEM_LIST_ID` | high |
| [PAT_ENC_HOSP_PROB](PAT_ENC_HOSP_PROB.md) | `PROBLEM_LIST_ID` | high |
| [PAT_PROBLEM_LIST](PAT_PROBLEM_LIST.md) | `PROBLEM_LIST_ID` | high |
| [PL_SYSTEMS](PL_SYSTEMS.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_DEL_TX_SUMM](PROBLEM_DEL_TX_SUMM.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_DISEASE_STATUS](PROBLEM_DISEASE_STATUS.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_DISEASE_STATUS_HX](PROBLEM_DISEASE_STATUS_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_DISEASE_STAT_EVID](PROBLEM_DISEASE_STAT_EVID.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_DIS_STAT_EVID_HX](PROBLEM_DIS_STAT_EVID_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_DIS_STAT_NOTE_HX](PROBLEM_DIS_STAT_NOTE_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_EVENTS](PROBLEM_EVENTS.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_EVENTS_AUD](PROBLEM_EVENTS_AUD.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_LIST_ALL](PROBLEM_LIST_ALL.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_LIST_HX](PROBLEM_LIST_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_NOTES](PROBLEM_NOTES.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_NOTE_PROPS](PROBLEM_NOTE_PROPS.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_STAGE_UPDATES](PROBLEM_STAGE_UPDATES.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_TREAT_SUMM_AUDIT](PROBLEM_TREAT_SUMM_AUDIT.md) | `PROBLEM_LIST_ID` | high |
| [PROBLEM_TREAT_SUMM_HNO_ID](PROBLEM_TREAT_SUMM_HNO_ID.md) | `PROBLEM_LIST_ID` | high |
| [PROB_DEL_STAGES](PROB_DEL_STAGES.md) | `PROBLEM_LIST_ID` | high |
| [PROB_DIS_STAT_END_DATE_HX](PROB_DIS_STAT_END_DATE_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROB_DIS_STAT_EPT_CSN_HX](PROB_DIS_STAT_EPT_CSN_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROB_DIS_STAT_START_DT_HX](PROB_DIS_STAT_START_DT_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROB_DIS_ST_ENTRY_INST_HX](PROB_DIS_ST_ENTRY_INST_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROB_DIS_ST_ENTRY_USER_HX](PROB_DIS_ST_ENTRY_USER_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROB_DIS_ST_ENTRY_WKFL_HX](PROB_DIS_ST_ENTRY_WKFL_HX.md) | `PROBLEM_LIST_ID` | high |
| [PROB_FILED_FORMS](PROB_FILED_FORMS.md) | `PROBLEM_LIST_ID` | high |
| [PROB_LNKSRC_ADM](PROB_LNKSRC_ADM.md) | `PROBLEM_LIST_ID` | high |
| [PROB_LNKSRC_ORD](PROB_LNKSRC_ORD.md) | `PROBLEM_LIST_ID` | high |
| [PROB_LNKSRC_ORL](PROB_LNKSRC_ORL.md) | `PROBLEM_LIST_ID` | high |
| [PROB_MODIFIERS](PROB_MODIFIERS.md) | `PROBLEM_LIST_ID` | high |
| [PROB_RELATED_GOALS](PROB_RELATED_GOALS.md) | `PROBLEM_LIST_ID` | high |
| [PROB_STAGES](PROB_STAGES.md) | `PROBLEM_LIST_ID` | high |
| [PROB_TXP_MODIFIERS](PROB_TXP_MODIFIERS.md) | `PROBLEM_LIST_ID` | high |
| [PROB_UPDATES](PROB_UPDATES.md) | `PROBLEM_LIST_ID` | high |
| [REJECT_TREAT](REJECT_TREAT.md) | `PROBLEM_LIST_ID` | high |
| [REJECT_TREAT_HX](REJECT_TREAT_HX.md) | `PROBLEM_LIST_ID` | high |
| [SDD_PROBLEMS](SDD_PROBLEMS.md) | `PROBLEM_LIST_ID` | high |
| [SMRTDTA_ELEM_PROBLEM](SMRTDTA_ELEM_PROBLEM.md) | `PROBLEM_LIST_ID` | high |
| [STENT_INSERTED_HX](STENT_INSERTED_HX.md) | `PROBLEM_LIST_ID` | high |
| [SYNDRO_SURV_EVENT_PROBS](SYNDRO_SURV_EVENT_PROBS.md) | `PROBLEM_LIST_ID` | high |

