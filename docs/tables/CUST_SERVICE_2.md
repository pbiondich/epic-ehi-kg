# CUST_SERVICE_2

> The CUST_SERVICE_2 table stores information entered into system's Customer Service module. This can be used to report on communication between medical facility staff and patients.

**Overflow of:** [CUST_SERVICE](CUST_SERVICE.md)  
**Primary key:** `COMM_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the communication record. |
| 2 | `SOURCE_BROKERAGE_ID` | VARCHAR |  | Stores the source agency record (AGY) for the customer service record. If a CRM is created in Tapestry Link by a broker, a source agency can be linked instead of a source provider. |
| 3 | `SOURCE_BROKERAGE_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 4 | `SUBJECT_AGENCY_ID` | VARCHAR |  | Stores the subject Agency (AGY) for the CRM. |
| 5 | `SUBJECT_AGENCY_ID_AGENCY_NAME` | VARCHAR |  | The name of the agency. |
| 6 | `SUBJECT_AGENT_ID_AGENT_NAME` | VARCHAR |  | The name of the agent. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

