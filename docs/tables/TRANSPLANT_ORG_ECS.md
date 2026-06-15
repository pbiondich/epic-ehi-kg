# TRANSPLANT_ORG_ECS

> This table contains information about a transplant patient's willingness to accept organs from donors meeting various criteria. Each line represents a change in the documentation about the patient's willingness to accept organs from donors meeting various criteria.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 26  
**Org-specific columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique ID of the episode of care record. |
| 2 | `LINE` | INTEGER | PK | Each line identifies a change to the type organ accepted selection. |
| 3 | `TX_HCV_YN` | VARCHAR |  | Whether or not the patient will accept an hepatitis C (HCV) positive organ. |
| 4 | `TX_HBV_YN` | VARCHAR |  | Whether or not the patient will accept a hepatitis B (HBV) positive organ. |
| 5 | `TX_ECD_YN` | VARCHAR |  | Whether or not the patient will accept an organ from an expanded criteria donor. |
| 6 | `TX_ECD_UPD_USER_ID` | VARCHAR |  | The user who updated patient's donor criteria. |
| 7 | `TX_ECD_UPD_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `TX_ECD_UPD_INST` | DATETIME (Local) |  | The instant when patient's donor criteria were documented. |
| 9 | `TX_HCV_REASON_C_NAME` | VARCHAR | org | The category number for the reason for accepting or not accepting an organ from a hepatitis C (HCV) positive donor. This category number is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 10 | `TX_HBV_REASON_C_NAME` | VARCHAR | org | The category number for the reason for accepting or not accepting an organ from a hepatitis B (HBV) positive donor. This category number is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 11 | `TX_ECD_REASON_C_NAME` | VARCHAR | org | The category number for the reason for accepting or not accepting an organ from an expanded criteria donor. This category number is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 12 | `TX_DOC_VERIFIER_ID` | VARCHAR |  | User who verifies the donor organ criteria |
| 13 | `TX_DOC_VERIFIER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 14 | `TX_DOC_VERIFY_INST` | DATETIME (Local) |  | Date the donor organ criteria was verified |
| 15 | `TX_CROSSMATCH_YN` | VARCHAR |  | Does transplant require a crossmatch |
| 16 | `TX_XMATCH_REASON_C_NAME` | VARCHAR | org | The category number for the reason the organ does or does not need crossmatch testing performed. This category number is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 17 | `TX_ANTIGENS_YN` | VARCHAR |  | Does the transplant have unacceptable antigens |
| 18 | `TX_ANTIGEN_REASON_C_NAME` | VARCHAR | org | The category number for the reason for the patient's unacceptable antigens. This category number is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 19 | `TX_DCD_YN` | VARCHAR |  | Whether the recipient will accept an organ from a donor who died from cardiac death. |
| 20 | `TX_DCD_REASON_C_NAME` | VARCHAR | org | The reason for accepting or not accepting a donation after cardiac death. |
| 21 | `MIN_DNR_WEIGHT` | NUMERIC |  | Minimum acceptable donor weight |
| 22 | `MAX_DNR_WEIGHT` | NUMERIC |  | Maximum acceptable donor weight |
| 23 | `CDC_HIGH_RISK_YN` | VARCHAR |  | Indicates whether the patient will accept an organ from a donor that has risk factors for blood-borne disease transmission. |
| 24 | `CDC_REASON_C_NAME` | VARCHAR | org | The reason a patient will or will not accept an organ from a donor that has risk factors for blood-borne disease transmission. |
| 25 | `SEGMENTAL_LIVER_YN` | VARCHAR |  | Indicates whether the patient will accept a segmental liver from a donor. |
| 26 | `SEG_LVR_REASON_C_NAME` | VARCHAR | org | The reason a patient will or will not accept a segmental liver as a donor organ. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

