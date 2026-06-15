# ORDER_RAD_RECPNT

> This table contains the recipients who were carbon copied on the imaging order results, along with ad hoc info, routing method, and address.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier of the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CC_RECIPIENTS_LIST` | VARCHAR |  | The recipient of results of this order. The data is in a carat delimited string of the form, "INI^ID^Recipient Name^System Flag". If the recipient is found in an Epic database, the INI and ID will be filled in. If the recipient is ad hoc (not in an Epic database), the INI and ID will be left blank. The System Flag contains settings used internally. |
| 4 | `CC_AD_HOC_INFO` | VARCHAR |  | The ad hoc recipient contact info in a "\|" delimited list. The format of this string is "Fax number\|Phone number\|Address\|City\|State ID\|ZIP\|Country ID". If the Address is on multiple lines, it is delimited by two spaces. This item is null when the recipient is not ad hoc. |
| 5 | `CC_ROUTE_METH_C_NAME` | VARCHAR | org | The results routing communication method category number for the order. This field describes how the result should be communicated out (ex. mail, fax, etc.). |
| 6 | `ROUTING_ADDRESS` | VARCHAR |  | If the recipient has an SER or EMP record with multiple addresses, this item contains a dash-delimited string with the SER or EMP .1 and the ID number of the address to which the result will be routed. This item is null when the recipient has no SER or EMP record. For SER recipients, the address ID corresponds to SER 21000, which is available in Clarity. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

