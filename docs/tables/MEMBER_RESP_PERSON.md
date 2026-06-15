# MEMBER_RESP_PERSON

> This table stores information about the responsible person (or people) for a member, as stored in the coverage. It includes information about name, SSN, relationship to members, and demographics. Each member on a coverage can have multiple responsible parties. The responsible parties for a specific member and coverage can be retrieved by joining to CVG_ID using a coverage ID and MEM_RESP_MEMBER_ID a patient ID. For example, MEMBER_RESP_PERSON.CVG_ID = COVERAGE_MEMBER_LIST.COVERAGE_ID AND MEMBER_RESP_PERSON.MEM_RESP_MEMBER_ID = COVERAGE_MEMBER_LIST.PAT_ID.

**Primary key:** `CVG_ID`, `LINE`  
**Columns:** 18  
**Org-specific columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CVG_ID` | NUMERIC | PK FK→ | The unique identifier for the coverage record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MEM_RESP_NAME` | VARCHAR |  | The name of the person responsible for the member. |
| 4 | `MEM_RESP_CITY` | VARCHAR |  | The city of the person responsible for the member. |
| 5 | `MEM_RESP_STATE_C_NAME` | VARCHAR | org | The state of the person responsible for the member. |
| 6 | `MEM_RESP_ZIP` | VARCHAR |  | The ZIP code of the person responsible for the member. |
| 7 | `MEM_RESP_COUNTY_C_NAME` | VARCHAR | org | The county of the person responsible for the member. |
| 8 | `MEM_RESP_COUNTRY_C_NAME` | VARCHAR | org | The country of the person responsible for the member. |
| 9 | `MEM_RESP_EMAIL` | VARCHAR |  | The e-mail address of the person responsible for the member. |
| 10 | `MEM_RESP_REL_C_NAME` | VARCHAR | org | The relationship between the member and the responsible person. |
| 11 | `MEM_RESP_MEMBER_ID` | VARCHAR |  | The internal ID of the member for whom a responsible person is responsible. |
| 12 | `MEM_RESP_ADDR_LN_1` | VARCHAR |  | This item contains line one of the member's responsible person address. The purpose of this item is to provide the ability for reporting administrators to retrieve line one of the address without having to join the member responsible person address table. |
| 13 | `MEM_RESP_ADDR_LN_2` | VARCHAR |  | This item contains line two of the member's responsible person address. The purpose of this item is to provide the ability for reporting administrators to retrieve line two of the address without having to join the member responsible person address table. |
| 14 | `MEM_RESP_HOUSE_NUM` | VARCHAR |  | The house number of the responsible person's address. |
| 15 | `MEM_RESP_DISTRICT_C_NAME` | VARCHAR | org | The district category ID of the responsible person's address. |
| 16 | `MEM_RESP_EFF_DATE` | DATETIME |  | The effective date on which person became responsible for the member. |
| 17 | `MEM_RESP_TERM_DATE` | DATETIME |  | The termination date on which person's responsibility for the member ends. |
| 18 | `MEM_RESP_GUID` | VARCHAR |  | The line ID of the person responsible for the member. Used to reference this line uniquely. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |

