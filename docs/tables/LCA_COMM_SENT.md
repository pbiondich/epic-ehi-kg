# LCA_COMM_SENT

> Table for LCA routing record that contains general information applicable to the entire route job. Essentially no add single response items.

**Primary key:** `COMMUNICATION_ID`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMMUNICATION_ID` | NUMERIC | PK shared | LCA routing record id |
| 2 | `COMM_INSTANT` | DATETIME (Local) |  | Time that the record was created |
| 3 | `SEND_STATUS_C_NAME` | VARCHAR | org | Sending status of the LCA communication record. Indicates whether sent or not. |
| 4 | `COMM_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Patient Contact ID (CSN) associated with the message. |
| 5 | `COMM_SENT_INST_UTC_DTTM` | DATETIME (UTC) |  | Instant the communication is sent. |
| 6 | `REP_DOCUMENT_CSN_ID` | NUMERIC |  | Store the DXR CSN that is being replied to by this message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COMM_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

