# PAS_TRIAGE_HX

> The triage history for the referral record.

**Primary key:** `REFERRAL_ID`, `LINE`  
**Columns:** 37  
**Org-specific columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The referral ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PAS_TRIAGE_HX_DEC_C_NAME` | VARCHAR |  | Referral triage history - triage decision |
| 4 | `PAS_TRIAGE_HX_PRI_C` | VARCHAR | org | Referral triage history - priority |
| 5 | `PAS_TRI_RJCT_RSN_C_NAME` | VARCHAR | org | Referral triage history - reject reason |
| 6 | `PAS_TRI_RD_SPEC_C_NAME` | VARCHAR | org | Referral triage history - redirect specialty |
| 7 | `PAS_TRI_HX_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `PAS_TRI_HX_SITE_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 9 | `PAS_TRI_HX_APPT_CMT` | VARCHAR |  | Referral triage information - appointment change comments |
| 10 | `PAS_TRI_HX_PW_UPG_YN` | VARCHAR |  | Referral triage history - pathway upgrade request history |
| 11 | `PAS_TRI_HX_USER_ID` | VARCHAR |  | Referral triage history - user |
| 12 | `PAS_TRI_HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `PAS_TRI_HX_INSTANT_DTTM` | DATETIME (UTC) |  | Referral triage history - instant of update |
| 14 | `PAS_TRI_HX_FREE_PX` | VARCHAR |  | Referral triage history - free text procedures |
| 15 | `PAS_TRI_HX_FREE_DX` | VARCHAR |  | PAS TRIAGE HISTORY - FREE TEXT DIAGNOSES |
| 16 | `TRIAGE_HX_RFL_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 17 | `TRIAGE_HX_ENC_TYPE_C_NAME` | VARCHAR | org | History item to track changes made to encounter type during triage. |
| 18 | `TRIAGE_HX_PACKAGE_TYPE_ID_EPISODE_DEF_NAME` | VARCHAR |  | This column displays the name of the episode / block definition record. |
| 19 | `TRIAGE_HX_TREATMENT_TYPE_C_NAME` | VARCHAR | org | History item to track changes made to treatment type during triage. |
| 20 | `TRIAGE_HX_RESP_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 21 | `TRIAGE_HX_PHASE_C_NAME` | VARCHAR | org | History item to track changes made to referral phase during referral triage |
| 22 | `TRIAGE_HX_RESP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 23 | `TRIAGE_HX_RESP_DEP_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 24 | `TRIAGE_HX_RFL_DX_TXT` | VARCHAR |  | History item to track changes made to free text associated with referral diagnoses during triage. |
| 25 | `TRIAGE_HX_REMIND_DATE` | DATETIME |  | An audit of when the user asked to be reminded of this referral. |
| 26 | `TRIAGE_HX_RECPNT_C_NAME` | VARCHAR |  | An audit of who a request for more information went to. |
| 27 | `PAS_TRI_RD_DEP_C_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 28 | `PAS_TRI_RD_PROVSP_C_NAME` | VARCHAR | org | Stores which provider specialty the patient was redirected to in triage |
| 29 | `TRIAGE_HX_UNACCEPT_REASON_C_NAME` | VARCHAR | org | Triage history item to track changes made to unaccept reason during referral triage. |
| 30 | `TRIAGE_HX_COND_GRP_C_NAME` | VARCHAR | org | Referral Triage History - Condition Group. |
| 31 | `TRIAGE_HX_RIGHT_TO_CARE_C_NAME` | VARCHAR | org | Referral Triage History - Right To Healthcare. |
| 32 | `TRIAGE_HX_RSLT_INIT_ASMT_C_NAME` | VARCHAR | org | Referral Triage History - Result of Initial Assessment |
| 33 | `PAS_TRI_HX_COND_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 34 | `PAS_TRI_HX_TRET_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 35 | `PAS_TRI_HX_SPEC_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 36 | `PAS_TRI_HX_SUBSP_GROUPER_ID_GROUPER_NAME` | VARCHAR |  | Record name |
| 37 | `TRIAGING_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

