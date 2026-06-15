# CLARITY_CONCEPT

> The CLARITY_CONCEPT table contains information pertaining to SmartData elements and concepts. SmartData elements are discrete data elements that can have data stored against them. Concepts are used as reference terminology, but should not be used for data storage. Each concept and element has a unique identifier (CUI), which is used as the primary key for the table.

**Primary key:** `CONCEPT_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CONCEPT_ID` | VARCHAR | PK | The SmartData identifier, such as MEDCIN#4104. |
| 2 | `NAME` | VARCHAR |  | The SmartData element name, such as "A Family History of Sickle Cell Anemia". |
| 3 | `ABBREVIATION` | VARCHAR |  | An abbreviation of the SmartData element's name. |
| 4 | `MASTER_FILE_LINK` | VARCHAR |  | The INI to which the SmartData element is linked. This should only be populated for networked SmartData elements. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

