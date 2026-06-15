# MC_CLAIM_PRICER

> This table contains core Epic Pricer information.

**Primary key:** `PRICER_MSG_ID`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier for the Epic Pricer message record. |
| 2 | `CLM_PRICER_REC_TYPE_C_NAME` | VARCHAR |  | The type of Epic Pricer record. The type determines the context of data specified on this record. |
| 3 | `PARENT_PRICER_MSG_ID` | NUMERIC |  | The parent record associated with this Epic Pricer message record. If the value of the ASSOC_TX_ID is not null, then this column will contain the unique identifier of the Epic Pricer message record for the claim that the service associated with this record is on. |
| 4 | `ASSOC_CLAIM_ID` | NUMERIC |  | The unique identifier for the claim associated with the Epic Pricer record. |
| 5 | `ASSOC_TX_ID` | NUMERIC |  | The unique identifier for the service line record associated with the Epic Pricer message record. |
| 6 | `ASSOC_PAT_ID` | VARCHAR | FK→ | The unique identifier for the member associated with the Epic Pricer message record. |
| 7 | `SERVICE_DATE` | DATETIME |  | For claim-level NPM records, this item stores the Claim Service From Date on the claim. For service-level NPM records, this item stores the Service From Date on the service. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASSOC_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |

