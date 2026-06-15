# LCA_COMM_ATTACH

> This table contains information regarding attachments sent in a communication routing job. Information includes the report ID of the report sent, the letter ID of a letter sent, a file name if a blob server was used, the attachment description, the attachment name and the ID of the fax report sent.

**Primary key:** `COMMUNICATION_ID`, `LINE`  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMMUNICATION_ID` | NUMERIC | PK shared | Internal ID for communication management routing for In Basket and Chart Review audit trail records. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMM_REPORT_ID` | VARCHAR |  | lrp report id of report sent in attachment |
| 4 | `COMM_REPORT_ID_REPORT_NAME` | VARCHAR |  | The name of the report |
| 5 | `LETTER_ID` | VARCHAR |  | hno letter id of letter sent in attachment |
| 6 | `OTHER_BLOB_IDS` | VARCHAR |  | file name if a blob server was used other than the letter |
| 7 | `LETTER_BLOB` | VARCHAR |  | file name if a letter blob server was used |
| 8 | `REPORT_BLOB` | VARCHAR |  | file name if a report blob server was used |
| 9 | `DESCR` | VARCHAR |  | description of the attachment |
| 10 | `ATTACHMENT_NAME` | VARCHAR |  | This column stores the attachment date (LCA-350). This typically stores the date listed in the first date column on the Chart Review tab. |
| 11 | `FAX_REPORT_ID` | VARCHAR |  | lrp id for faxes sent in the attachment |
| 12 | `FAX_REPORT_ID_REPORT_NAME` | VARCHAR |  | The name of the report |
| 13 | `PAT_ENC_CSN` | NUMERIC | FK→ | The column serves as a link to EPT encounters whose reports/notes might have resulted in the creation of the LCA record. |
| 14 | `HNO_CSN` | NUMERIC |  | CSN of a note that was routed |
| 15 | `EPISODE_ID` | NUMERIC | FK→ | This item stores the ID of the routed Episode. |
| 16 | `DXR_ID` | NUMERIC |  | This item stores the ID of the routed DXR. |
| 17 | `LCA_COMM_LNO_ID` | NUMERIC |  | Stores the LNO ID of the Patient Summary Extract routed from Chart Review |
| 18 | `ORDER_ID` | NUMERIC | shared | Contains the ORD ID of the order routed from Chart Review |
| 19 | `REFERRAL_ID` | NUMERIC | FK→ | Contains the RFL ID of the referral routed from Chart Review |
| 20 | `DOCUMENT_ID` | VARCHAR | shared | Contains the DCS ID of the document/media routed from Chart Review |
| 21 | `IS_SUM_OF_CARE_ATTCHMENT_YN` | VARCHAR |  | Whether this attachment is a Summary of Care |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EPISODE_ID` | [EPISODE](EPISODE.md) | name_stem | high |
| `PAT_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | sole_pk | high |
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

