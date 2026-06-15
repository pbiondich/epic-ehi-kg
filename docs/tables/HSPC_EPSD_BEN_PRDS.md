# HSPC_EPSD_BEN_PRDS

> This table extracts data about hospice benefit periods.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | Unique identifier for the summary block record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BNFT_PRD_START_DATE` | DATETIME |  | This item tracks the start date of each hospice benefit period for the hospice admission associated with the episode. |
| 4 | `BNFT_PRD_END_DATE` | DATETIME |  | This item tracks the end date of each hospice benefit period for the hospice admission associated with the episode. |
| 5 | `BNFT_PRD_COMMENTS` | VARCHAR |  | This item tracks free text comments about a hospice benefit period. |
| 6 | `BNFT_PRD_CTI_ID` | VARCHAR |  | This item tracks the ID of the Certificate of Terminal Illness verbal order that corresponds to this hospice benefit period. |
| 7 | `BNFT_PRD_NUM` | INTEGER |  | This item tracks the hospice benefit period number for the hospice admission associated with the episode. |
| 8 | `BNFT_PRD_F2F_ID` | VARCHAR |  | The unique identifier of the Face to Face verbal order record that corresponds to this hospice benefit period. |
| 9 | `BNFT_PRD_VCTI_DT` | DATETIME |  | The date of the verbal CTI that corresponds to this benefit period. |
| 10 | `BNFT_PD_VCTI_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 11 | `BT_PD_VCTI_RCVR_ID` | VARCHAR |  | The unique identifier of the user who received the verbal certificate of illness (CTI) from the provider. |
| 12 | `BT_PD_VCTI_RCVR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 13 | `BNFT_PRD_2ND_VCTI_DT` | DATETIME |  | The date of the second verbal certificate of terminal illness (CTI). |
| 14 | `BNFT_PRD_2ND_VCTI_SER_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 15 | `BNFT_PRD_2ND_VCTI_RCVR_ID` | VARCHAR |  | The person who received the second verbal certificate of illness (CTI) from the provider. |
| 16 | `BNFT_PRD_2ND_VCTI_RCVR_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 17 | `BNFT_PRD_VCTI_NOTE_ID` | VARCHAR |  | The unique identifier of the note record associated with the first verbal CTI for this hospice benefit period. |
| 18 | `BNFT_PRD_2ND_VCTI_NOTE_ID` | VARCHAR |  | The unique ID of the note associated with the second verbal Certificate of Terminal Illness. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

