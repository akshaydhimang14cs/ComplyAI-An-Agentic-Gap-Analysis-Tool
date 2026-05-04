# ComlyAI: An Agentic Gap Analysis.

Framework: ISO 27001:2022 Annex A
Generated at: 2026-04-27T20:06:25

## Overview

This report presents the final automated gap analysis for ISO 27001:2022 Annex A controls against the organisation's Statement of Applicability, scope context, business objectives, and available evidence.

## Stage 1

- Total number of controls available as per security framework: 93
- Total number of controls Available as per organisation's SOA: 93
- Total number of controls Implemented as per organisation's SOA: 37
- Total number of controls partially implemented by the organisation as per SOA: 55
- Total number of controls not implemented by the organisation as per SOA: 1

## Stage 3

- Total controls evaluated: 93
- Applicable: 93
- Not required: 0
- Implemented: 39
- Partially implemented: 53
- Not implemented: 1
- LLM Decision marked not required: 0

## Priority Findings

### A.8.11 - Data masking

- Domain: Technological
- Applicability decision: Applicable
- LLM Decision: Not Implemented
- Evidence summary: The SoA marks the control as applicable and clearly inside scope, but there is no explicit evidence of implementation.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement data masking techniques to limit exposure of sensitive taxpayer information in non-production environments.

### A.5.6 - Contact with special interest groups

- Domain: Organisational
- Applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented as it aligns with the business objectives and follows vendor advisories, but further engagement with professional groups is recommended to ensure full implementation.

### A.5.7 - Threat intelligence

- Domain: Organisational
- Applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence summary: The SoA marks the control as applicable and clearly inside scope, but lacks explicit evidence of implementation.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement a documented threat intelligence process tailored to tax administration services within the next 6 months.

### A.5.8 - Information security in project management

- Domain: Organisational
- Applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence summary: The SoA marks the control as applicable and clearly inside scope, but there is no explicit evidence of implementation.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement security controls based on ISO/IEC 27001 Annex A and relevant standards tailored to ABC’s context.

### A.5.9 - Inventory of information and other associated assets

- Domain: Organisational
- Applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence summary: The control is applicable as it falls within the scope of the Information Security Management System (ISMS) and has a clear implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, with evidence supporting its creation. Further efforts are needed to complete the asset register for all endpoints and cloud resources.

### A.5.13 - Labelling of information

- Domain: Organisational
- Applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence summary: Evidence supported the decision: A classification scheme (e.g., Public, Internal, Confidential, Highly Confidential) shall be established.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented. Further efforts are needed to establish a consistent labelling practice across all systems.

### A.5.14 - Information transfer

- Domain: Organisational
- Applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence summary: Evidence supported the decision: Risk treatment options shall include avoiding, reducing, transferring, or accepting risks, with justification and approval recorded.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Complete the remaining implementation activities and retain direct evidence that the control is operating as intended.

### A.5.16 - Identity management

- Domain: Organisational
- Applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The Identity Management control is Partially Implemented.

### A.5.18 - Access rights

- Domain: Organisational
- Applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence summary: Evidence supported the decision: Access rights are defined conceptually and based on least privilege but detailed role-based access matrices and periodic reviews are still being formalised.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, as evidenced by the existence of access control policy documents (ISMS_Policy_ABC_corporation.txt and AccessControlPolicy.txt). Further implementation is recommended to formalize detailed role-based access matrices and periodic reviews.

### A.5.19 - Information security in supplier relationships

- Domain: Organisational
- Applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence summary: The SoA marks the control as applicable and clearly inside scope, but lacks explicit evidence of implementation.
- Gap note: No material gap is observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Not Implemented

## Domain-wise Detailed Analysis

### Organisational

#### A.5.1 - Policies for information security

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Top management shall define and review measurable information security objectives that are consistent with this policy and ABC’s strategic direction, such as: | The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli...
- Evidence summary: The scope statement clearly defines the Information Security Management System (ISMS) for ABC Corporation, and the SoA justification supports the implementation of this control.
- Gap note: No material gap observed.
- Recommendation: No material gap is observed.

#### A.5.2 - Information security roles and responsibilities

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Roles and responsibilities related to information security shall be defined and documented in job descriptions or contracts. | Internal factors such as organisational structure, roles and capabilities, information systems, and service delivery processes.
- Evidence summary: The control is applicable as it aligns with the Information Security Management System (ISMS) scope statement.
- Gap note: No material gap observed.
- Recommendation: The implementation of the information security roles and responsibilities control is confirmed to be implemented.

#### A.5.3 - Segregation of duties

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Coordinating risk assessments, risk treatment, and control implementation. | Apply a risk‑based approach to the selection and implementation of information security controls.
- Evidence summary: Evidence supported the decision: Coordinating risk assessments, risk treatment, and control implementation.
- Gap note: ...
- Recommendation: The Segregation of duties control is Applicable. The SoA justification provides sufficient context for this decision.

#### A.5.4 - Management responsibilities

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Provide appropriate resources and support for information security activities. | This policy shall be documented, controlled, and made available to all relevant personnel.
- Evidence summary: Evidence supported the decision: Top management approves ISMS policy sets objectives, allocates resources, and performs management review.
- Gap note: No material gap observed.
- Recommendation: The control is implemented as per the SoA justification. No further action is required.

#### A.5.5 - Contact with authorities

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: All personnel shall be encouraged and enabled to report suspected or actual security incidents or weaknesses. | Where required, incidents shall be reported to affected clients and, if applicable, regulatory authorities, in line with contractual and legal obligations.
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation.
- Gap note: No material gap observed.
- Recommendation: The control is Applicable.

#### A.5.6 - Contact with special interest groups

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: ABC shall determine the needs and expectations of interested parties relevant to information security, including government tax authorities, taxpayers, employees, suppliers, regulators, and other partners. | Apply a risk‑based approach to the selection and implementation of information security controls.
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented as it aligns with the business objectives and follows vendor advisories, but further engagement with professional groups is recommended to ensure full implementation.

#### A.5.7 - Threat intelligence

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Apply a risk‑based approach to the selection and implementation of information security controls. | ABC shall adopt and maintain a documented information security risk assessment methodology defining risk criteria, likelihood and impact scales, and risk acceptance criteria.
- Evidence summary: The SoA marks the control as applicable and clearly inside scope, but lacks explicit evidence of implementation.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement a documented threat intelligence process tailored to tax administration services within the next 6 months.

#### A.5.8 - Information security in project management

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Risks to confidentiality, integrity, and availability of information within the ISMS scope shall be identified, analysed, and evaluated using a documented risk assessment methodology. | Security controls shall be selected based on ISO/IEC 27001 Annex A and other relevant standards, tailored to ABC’s context.
- Evidence summary: The SoA marks the control as applicable and clearly inside scope, but there is no explicit evidence of implementation.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement security controls based on ISO/IEC 27001 Annex A and relevant standards tailored to ABC’s context.

#### A.5.9 - Inventory of information and other associated assets

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Risks to confidentiality, integrity, and availability of information within the ISMS scope shall be identified, analysed, and evaluated using a documented risk assessment methodology. | ABC shall adopt and maintain a documented information security risk assessment methodology defining risk criteria, likelihood and impact scales, and risk acceptance criteria.
- Evidence summary: The control is applicable as it falls within the scope of the Information Security Management System (ISMS) and has a clear implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, with evidence supporting its creation. Further efforts are needed to complete the asset register for all endpoints and cloud resources.

#### A.5.10 - Acceptable use of information and other associated assets

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: ABC shall define acceptable use rules for IT assets and services: | Protecting information and assets under their control.
- Evidence summary: Evidence supported the decision: Mapped documents ISMS_Policy_ABC_corporation.txt Acceptable Use Policy.txt.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented, as it is clear that employees and contractors must follow acceptable use rules for devices networks and client data. No material gap is observed.

#### A.5.11 - Return of assets

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: ABC and client assets (equipment, ID cards, access tokens, documents) shall be returned. | Upon termination or role change, access rights shall be adjusted or revoked promptly.
- Evidence summary: The control is clearly inside scope and the SoA marks it as applicable.
- Gap note: No material gap observed.
- Recommendation: The control is implemented, with clear evidence supporting its effectiveness in ensuring the return of assets upon termination or role change.

#### A.5.12 - Classification of information

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: ABC will ensure that physical locations under its control that host or access information within the ISMS scope are appropriately protected: | Access to ABC and client systems shall be controlled to ensure that only authorized individuals have appropriate levels of access:
- Evidence summary: Evidence supported the decision: Mapped documents ISMS_Policy_ABC_corporation.txt and Information Classification and Handling Procedure.txt.
- Gap note: No material gap observed.
- Recommendation: The control is implemented as per the SoA justification.

#### A.5.13 - Labelling of information

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: A classification scheme (e.g., Public, Internal, Confidential, Highly Confidential) shall be established. | Client‑owned taxpayer and departmental data shall be classified as at least Confidential, or as specified by the client.
- Evidence summary: Evidence supported the decision: A classification scheme (e.g., Public, Internal, Confidential, Highly Confidential) shall be established.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented. Further efforts are needed to establish a consistent labelling practice across all systems.

#### A.5.14 - Information transfer

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Risk treatment options shall include avoiding, reducing, transferring, or accepting risks, with justification and approval recorded. | Firewalls, secure configurations, and access controls shall be applied to networks under ABC control.
- Evidence summary: Evidence supported the decision: Risk treatment options shall include avoiding, reducing, transferring, or accepting risks, with justification and approval recorded.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Complete the remaining implementation activities and retain direct evidence that the control is operating as intended.

#### A.5.15 - Access control

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli... | Access rights shall follow the principle of least privilege and be periodically reviewed.
- Evidence summary: The scope statement clearly defines the scope of access control, and the SoA justification provides context for implementing this control.
- Gap note: No material gap observed.
- Recommendation: No material gap is observed.

#### A.5.16 - Identity management

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Users shall not attempt to bypass security controls, install unauthorized software, or use ABC or client systems for illegal or unethical activities. | Each asset shall have an identified owner responsible for ensuring appropriate protection, classification, and lifecycle management.
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The Identity Management control is Partially Implemented.

#### A.5.17 - Authentication information

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Strong authentication mechanisms (e.g., complex passwords, MFA where feasible) shall be implemented, especially for administrative and remote access. | Privileged access shall be strictly controlled, logged, and monitored.
- Evidence summary: Evidence supported the decision: Strong authentication mechanisms and privileged access controls are in place.
- Gap note: No material gap observed.
- Recommendation: The control is implemented as per the SoA justification, with strong authentication mechanisms and privileged access controls in place. No further action is required.

#### A.5.18 - Access rights

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Access rights shall be reviewed at periodic intervals and adjusted when roles change. | Access rights to applications, systems, and data shall be granted on a need‑to‑know and least‑privilege basis, and approved by responsible managers.
- Evidence summary: Evidence supported the decision: Access rights are defined conceptually and based on least privilege but detailed role-based access matrices and periodic reviews are still being formalised.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, as evidenced by the existence of access control policy documents (ISMS_Policy_ABC_corporation.txt and AccessControlPolicy.txt). Further implementation is recommended to formalize detailed role-based access matrices and periodic reviews.

#### A.5.19 - Information security in supplier relationships

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Information security requirements shall be included in contracts and agreements. | ABC shall determine the needs and expectations of interested parties relevant to information security, including government tax authorities, taxpayers, employees, suppliers, regulators, and other partners.
- Evidence summary: The SoA marks the control as applicable and clearly inside scope, but lacks explicit evidence of implementation.
- Gap note: No material gap is observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Not Implemented

#### A.5.20 - Addressing information security within supplier agreements

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Information security requirements shall be included in contracts and agreements. | Obligations arising from client contracts and service level agreements shall be explicitly captured and communicated to relevant teams.
- Evidence summary: Evidence supported the decision: Contracts with hosting and cloud providers include confidentiality security and incident notification requirements.
- Gap note: No material gap observed.
- Recommendation: The control is Applicable.

#### A.5.21 - Managing information security in the ICT supply chain

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: ABC will maintain a systematic approach to managing information security risks: | Information security requirements shall be included in contracts and agreements.
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, as indicated by the SoA's 'Partially Implemented' status. Further evidence is required to confirm full implementation.

#### A.5.22 - Monitoring review and change management of supplier services

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Management reviews shall consider the status of actions from previous reviews, changes in external and internal issues, fulfilment of information security objectives, results of monitoring and measurement, audit resul... | ABC shall continually improve the suitability, adequacy, and effectiveness of the ISMS by using the results of monitoring, audits, incidents, and management reviews.
- Evidence summary: The SoA marks the control as applicable and clearly inside scope.
- Gap note: No material gap is observed.
- Recommendation: The implementation of monitoring, review and change management of supplier services is fully implemented.

#### A.5.23 - Information security for use of cloud services

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Where ABC uses cloud or other outsourced services, contractual clauses shall address information security requirements and responsibilities. | The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli...
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, as ABC Corporation has high-level controls in place but a dedicated cloud security standard is still being developed. Further development of this standard should be considered to ensure full applicability and effectiveness.

#### A.5.24 - Information security incident management planning and preparation

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Coordinating response to significant information security incidents. | Reporting suspected information security incidents, weaknesses, or policy violations without delay.
- Evidence summary: Evidence supported the decision: ABC has defined roles contact points and high level procedures for handling security incidents affecting tax portals.
- Gap note: ...
- Recommendation: The control is Applicable as it meets the requirements of ISO A.5.24, Information security incident management planning and preparation. The implementation status is Implemented.

#### A.5.25 - Assessment and decision on information security events

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Coordinating response to significant information security incidents. | ABC shall adopt and maintain a documented information security risk assessment methodology defining risk criteria, likelihood and impact scales, and risk acceptance criteria.
- Evidence summary: The control is clearly inside scope and marked as applicable by the SoA.
- Gap note: No material gap observed.
- Recommendation: No material gap observed.

#### A.5.26 - Response to information security incidents

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Coordinating response to significant information security incidents. | Reporting suspected information security incidents, weaknesses, or policy violations without delay.
- Evidence summary: Evidence supported the decision: Coordinating response to significant information security incidents and reporting suspected information security incidents, weaknesses, or policy violations without delay.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.5.27 - Learning from information security incidents

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Root cause analysis shall be performed for significant incidents, and corrective actions implemented to prevent recurrence. | Coordinating response to significant information security incidents.
- Evidence summary: Evidence supported the decision: Major incidents lead to lessons learned but a consistent post incident review template and tracking for all incidents is still being established.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Complete the remaining implementation activities and retain direct evidence that the control is operating as intended.

#### A.5.28 - Collection of evidence

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Implementing and maintaining security controls on servers, databases, networks, and supporting infrastructure. | Reporting suspected information security incidents, weaknesses, or policy violations without delay.
- Evidence summary: Evidence supported the decision: Implementing and maintaining security controls on servers, databases, networks, and supporting infrastructure.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented. Further implementation of formalised digital evidence handling procedures is recommended to ensure compliance with ISO 27001:2022.

#### A.5.29 - Information security during disruption

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Apply a risk‑based approach to the selection and implementation of information security controls. | Implementing and maintaining security controls on servers, databases, networks, and supporting infrastructure.
- Evidence summary: Evidence supported the decision: Business continuity and DR plans exist for critical systems.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented.

#### A.5.30 - ICT readiness for business continuity

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Business continuity and disaster recovery strategies shall be defined for critical systems, including the taxpayer and department portals. | Business impact analysis shall identify critical services and acceptable recovery objectives.
- Evidence summary: The SoA marks the control as applicable and clearly inside scope, but lacks explicit evidence of implementation.
- Gap note: No material gap is observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control should be implemented to ensure ICT systems have sufficient resilience to support business continuity objectives.

#### A.5.31 - Identification of legal statutory regulatory and contractual requirements

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Non‑compliance with legal, regulatory, or contractual obligations shall be addressed through corrective actions and, where necessary, reported to appropriate authorities or clients. | Obligations arising from client contracts and service level agreements shall be explicitly captured and communicated to relevant teams.
- Evidence summary: Scope statement and SoA justification provide clear evidence that the control is applicable.
- Gap note: No material gap observed.
- Recommendation: No material gap observed.

#### A.5.32 - Intellectual property rights

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Compliance with laws, regulations, and contracts | ABC will ensure that physical locations under its control that host or access information within the ISMS scope are appropriately protected:
- Evidence summary: Evidence supported the decision: Compliance with laws, regulations, and contracts.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented as it ensures compliance with IP laws through formal IP compliance monitoring. Further strengthening of this control is recommended.

#### A.5.33 - Protection of records

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Termination of supplier relationships shall include secure return or destruction of data and revocation of access. | Visitor access shall be controlled and recorded where applicable.
- Evidence summary: Evidence supported the decision: Termination of supplier relationships shall include secure return or destruction of data and revocation of access.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.5.34 - Privacy and protection of PII

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Information privacy and protection of personal data | ABC shall adopt and maintain a documented information security risk assessment methodology defining risk criteria, likelihood and impact scales, and risk acceptance criteria.
- Evidence summary: Evidence supported the decision: ISMS_Policy_ABC_corporation.txtPrivacyPolicy.txt
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.5.35 - Independent review of information security

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Apply a risk‑based approach to the selection and implementation of information security controls. | Security controls shall be selected based on ISO/IEC 27001 Annex A and other relevant standards, tailored to ABC’s context.
- Evidence summary: Evidence snippets supported the decision to implement control.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented as internal reviews occur but independent external audits are scheduled annually.

#### A.5.36 - Compliance with policies and standards for information security

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: All ISMS policies, procedures, standards, guidelines, records and other documented information shall be controlled. | All employees and relevant contractors shall receive regular training on information security, appropriate to their role and responsibilities.
- Evidence summary: Evidence supported the decision: ISMS_Policy_ABC_corporation.txt, InternalAuditProcedure.txt.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented due to limited automated monitoring and insufficient evidence of regular training for employees and contractors.

#### A.5.37 - Documented operating procedures

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: All ISMS policies, procedures, standards, guidelines, records and other documented information shall be controlled. | Standard operating procedures shall be documented for key operational tasks.
- Evidence summary: The control is clearly inside scope and the SoA marks it as applicable.
- Gap note: No material gap observed.
- Recommendation: No material gap observed.

### people

#### A.6.1 - Screening

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Background checks, where legally permitted and appropriate to the role, shall be conducted for employees and contractors with access to sensitive information or systems. | Roles and responsibilities related to information security shall be defined and documented in job descriptions or contracts.
- Evidence summary: Background screening is conducted for permanent staff in sensitive roles but the process for contractors and temporary staff is not fully standardised.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Complete the remaining implementation activities and retain direct evidence that the control is operating as intended.

#### A.6.2 - Terms and conditions of employment

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Information security requirements shall be included in contracts and agreements. | The formal scope of the ISMS, including boundaries and applicability, is defined in the separate document “Information Security Management System – Scope Statement for ABC Corporation”.
- Evidence summary: Employment contracts and NDAs include information security and confidentiality clauses covering systems and data within the ISMS scope.
- Gap note: ...
- Recommendation: The employment contracts and NDAs for ABC Corporation are clearly included in the Information Security Management System – Scope Statement, making them part of the ISMS. Therefore, it is recommended that this control be marked as Implemented.

#### A.6.3 - Information security awareness education and training

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: All personnel shall receive information security awareness training during induction and at regular intervals. | All employees and relevant contractors shall receive regular training on information security, appropriate to their role and responsibilities.
- Evidence summary: The scope statement clearly defines the information security management system's scope, and the SoA justification provides context for the control.
- Gap note: The control appears to exist, but implementation coverage or supporting evidence is incomplete. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented due to the need for stronger evidence of role-specific training for developers and admins. Further implementation efforts are recommended.

#### A.6.4 - Disciplinary process

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli... | This policy establishes the foundation of ABC’s Information Security Management System (ISMS) in alignment with ISO/IEC 27001:2022.
- Evidence summary: The scope statement clearly defines the Information Security Management System (ISMS) and the HR policy that establishes the disciplinary process.
- Gap note: No material gap is observed.
- Recommendation: Not Implemented

#### A.6.5 - Responsibilities after termination or change of employment

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: ABC shall determine the needs and expectations of interested parties relevant to information security, including government tax authorities, taxpayers, employees, suppliers, regulators, and other partners. | Where ABC uses cloud or other outsourced services, contractual clauses shall address information security requirements and responsibilities.
- Evidence summary: Evidence supported the decision: ABC shall determine the needs and expectations of interested parties relevant to information security, including government tax authorities, taxpayers, employees, suppliers, regulators, and other partners.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.6.6 - Confidentiality or non-disclosure agreements

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Documented information shall be approved prior to issue, kept up to date, protected from loss of confidentiality, integrity, or availability, and retained for as long as required by legal, regulatory, contractual, or... | ABC Corporation is committed to protecting the confidentiality, integrity, and availability of information entrusted to it by its clients, partners, and other interested parties.
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation.
- Gap note: No material gap observed.
- Recommendation: The control is implemented as per the Scope Statement and SoA. No further action is required.

#### A.6.7 - Remote working

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli... | This policy establishes the foundation of ABC’s Information Security Management System (ISMS) in alignment with ISO/IEC 27001:2022.
- Evidence summary: The scope statement clearly defines the remote working policy, but the implementation status is partially implemented.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement the remote working security standard as outlined in the ISMS_Policy_ABC_corporation.txt file.

#### A.6.8 - Information security event reporting by employees

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Reporting suspected information security incidents, weaknesses, or policy violations without delay. | All personnel shall be encouraged and enabled to report suspected or actual security incidents or weaknesses.
- Evidence summary: The control is clearly inside scope and marked as applicable by the SoA.
- Gap note: No material gap observed.
- Recommendation: No material gap observed.

### Physical

#### A.7.1 - Physical security perimeters

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli... | ABC will ensure that physical locations under its control that host or access information within the ISMS scope are appropriately protected:
- Evidence summary: The scope statement clearly defines the physical security perimeters for ABC Corporation, but the implementation status is partially implemented.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: ABC should continue to implement the Physical security perimeters control as Partially Implemented.

#### A.7.2 - Physical entry

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: ABC will ensure that physical locations under its control that host or access information within the ISMS scope are appropriately protected: | Access to server rooms, network equipment, and other critical facilities shall be restricted to authorized personnel.
- Evidence summary: The control is clearly inside scope and marked as applicable by the SoA.
- Gap note: No material gap observed.
- Recommendation: No material gap observed.

#### A.7.3 - Securing offices, rooms and facilities

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Access to server rooms, network equipment, and other critical facilities shall be restricted to authorized personnel. | Reasonable physical protections (locks, secure storage, etc.) shall be implemented.
- Evidence summary: Evidence supported the decision: Access to server rooms, network equipment, and other critical facilities shall be restricted to authorized personnel.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented. The SoA's justification for not implementing all key areas of physical security is sufficient, but further implementation is needed to ensure consistent documented security controls. Further investigation is recommended.

#### A.7.4 - Physical security monitoring

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Users shall not attempt to bypass security controls, install unauthorized software, or use ABC or client systems for illegal or unethical activities. | Logs shall be protected from unauthorized access, tampering, and premature deletion.
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, as evidenced by existing CCTV and basic physical monitoring at key sites and in third-party data centres. Further development of a formal monitoring standard and central review process is recommended to ensure the control meets the required standards.

#### A.7.5 - Protecting against physical and environmental threats

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Reasonable physical protections (locks, secure storage, etc.) shall be implemented. | Environmental controls (power protection, air conditioning, fire detection and suppression where applicable) shall be considered for critical equipment.
- Evidence summary: Reasonable physical protections and environmental controls were considered in the SoA, but no formal risk-based standard is being developed.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented as it includes reasonable physical protections and environmental controls. Further development of a formal risk-based standard may be necessary to ensure adequate protection against physical and environmental threats.

#### A.7.6 - Working in secure areas

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Access by supplier personnel to ABC or client systems shall be controlled and reviewed. | Where development or operations are outsourced, ABC shall assess and, where appropriate, monitor the supplier’s security measures.
- Evidence summary: Evidence supported the decision: Access by supplier personnel to ABC or client systems shall be controlled and reviewed.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented.

#### A.7.7 - Clear desk and clear screen

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Company and client‑provided assets (e.g., laptops, desktops, mobile devices, network access) shall be used for authorized business purposes only. | Use of personal devices to access ABC or client systems shall be governed by separate BYOD or remote access policies, if permitted.
- Evidence summary: The control is clearly inside scope and marked as applicable by the SoA.
- Gap note: The control appears to exist, but implementation coverage or supporting evidence is incomplete. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement clear desk and clear screen policies through a systematic approach, including training for staff and periodic checks of clear desk/clear screen practices.

#### A.7.8 - Equipment siting and protection

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Environmental controls (power protection, air conditioning, fire detection and suppression where applicable) shall be considered for critical equipment. | Access to server rooms, network equipment, and other critical facilities shall be restricted to authorized personnel.
- Evidence summary: The control is applicable due to the presence of environmental controls and access restrictions.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The implementation status should be updated to reflect the SoA's justification, which indicates that critical equipment requires some level of siting and protection. Further investigation may be necessary to determine the full extent of control implementation.

#### A.7.9 - Security of assets off-premises

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Company and client‑provided assets (e.g., laptops, desktops, mobile devices, network access) shall be used for authorized business purposes only. | The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli...
- Evidence summary: Evidence supported the decision: Company and client-provided assets (e.g., laptops, desktops, mobile devices, network access) shall be used for authorized business purposes only.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented due to the lack of a comprehensive policy for off-site asset protection and tracking. Further guidance from the SoA on implementing this control is recommended.

#### A.7.10 - Storage media

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Handling rules shall cover storage, transmission, sharing, display, printing, and disposal of information. | A classification scheme (e.g., Public, Internal, Confidential, Highly Confidential) shall be established.
- Evidence summary: Evidence supported the decision: Storage media handling is covered at a high level, but formal lifecycle management and documentation for issuing, transporting and returning media are still being strengthened.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented. Further efforts are needed to strengthen formal lifecycle management and documentation for storage media handling.

#### A.7.11 - Supporting utilities

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Environmental controls (power protection, air conditioning, fire detection and suppression where applicable) shall be considered for critical equipment. | Systems shall be protected against malware through use of up‑to‑date protection tools and safe operating practices.
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, as evidenced by the SoA's mention of monitoring and protection in data centres. However, further documentation on utility resilience requirements and testing is needed to support full implementation.

#### A.7.12 - Cabling security

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Systems shall be protected against malware through use of up‑to‑date protection tools and safe operating practices. | Data in transit over untrusted networks (e.g., internet) shall be protected using appropriate encryption (e.g., TLS).
- Evidence summary: The control is clearly inside scope and evidence snippets support its implementation.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement the control to protect power, data, and communications cables from interception, interference, or damage.

#### A.7.13 - Equipment maintenance

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Risks to confidentiality, integrity, and availability of information within the ISMS scope shall be identified, analysed, and evaluated using a documented risk assessment methodology. | Documented information shall be approved prior to issue, kept up to date, protected from loss of confidentiality, integrity, or availability, and retained for as long as required by legal, regulatory, contractual, or...
- Evidence summary: Evidence supported the decision: SoA justification provided context for control implementation.
- Gap note: No material gap observed.
- Recommendation: The control is implemented as per the Scope Statement and SoA. No further action is required.

#### A.7.14 - Secure disposal or re-use of equipment

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Backups of critical systems and data shall be performed regularly, stored securely, and tested for successful restore at planned intervals. | Encryption shall be used where appropriate, particularly for sensitive data in transit over untrusted networks and, when required, at rest.
- Evidence summary: Evidence supported the decision: Backups of critical systems and data shall be performed regularly, stored securely, and tested for successful restore at planned intervals. Encryption shall be used where appropriate.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented due to lack of consistently captured chain-of-custody documentation and evidence of destruction.

### Technological

#### A.8.1 - User endpoint devices

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli... | This policy establishes the foundation of ABC’s Information Security Management System (ISMS) in alignment with ISO/IEC 27001:2022.
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented due to progress on hardening laptops and a full EDR rollout still in progress.

#### A.8.2 - Privileged access rights

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: User IDs shall be unique to individuals; generic and shared accounts shall be restricted and justified. | Access rights to applications, systems, and data shall be granted on a need‑to‑know and least‑privilege basis, and approved by responsible managers.
- Evidence summary: Evidence supported the decision: User IDs shall be unique to individuals; generic and shared accounts shall be restricted and justified.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.8.3 - Information access restriction

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Protecting information and assets under their control. | Access to server rooms, network equipment, and other critical facilities shall be restricted to authorized personnel.
- Evidence summary: Evidence supported the decision: Access to server rooms, network equipment, and other critical facilities shall be restricted to authorized personnel.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.8.4 - Access to source code

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Changes to production systems shall follow a formal change management process, including assessment, approval, testing, and back‑out planning. | Development, test, and production environments shall be separated to reduce risk of unintended changes or data leakage.
- Evidence summary: Evidence supported the decision: Changes to production systems follow a formal change management process, and development, test, and production environments are separated.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented. The SoA justification provides context for this implementation status, but no material evidence supports full implementation. Further strengthening of access controls and standardization of external access rules would be necessary to meet the requirements.

#### A.8.5 - Secure authentication

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Strong authentication mechanisms (e.g., complex passwords, MFA where feasible) shall be implemented, especially for administrative and remote access. | Remote access to internal systems shall use secure channels (e.g., VPN with strong authentication).
- Evidence summary: The control is not fully implemented due to the lack of consistent MFA coverage for all critical systems.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement strong authentication mechanisms, especially for administrative and remote access, using secure channels (e.g., VPN with strong authentication).

#### A.8.6 - Capacity management

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli... | This policy establishes the foundation of ABC’s Information Security Management System (ISMS) in alignment with ISO/IEC 27001:2022.
- Evidence summary: The scope of the control is clearly defined in the SoA, and evidence supports the implementation of capacity management.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Complete the remaining implementation activities and retain direct evidence that the control is operating as intended.

#### A.8.7 - Protection against malware

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Systems shall be protected against malware through use of up‑to‑date protection tools and safe operating practices. | Reasonable physical protections (locks, secure storage, etc.) shall be implemented.
- Evidence summary: Evidence supported the decision: Systems shall be protected against malware through use of up-to-date protection tools and safe operating practices.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented, as it is clear from the SoA that endpoint protection and secure browsing controls are deployed and kept up to date.

#### A.8.8 - Management of technical vulnerabilities

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Risks to confidentiality, integrity, and availability of information within the ISMS scope shall be identified, analysed, and evaluated using a documented risk assessment methodology. | Residual risk and risk treatment plans shall be approved by appropriate management.
- Evidence summary: Evidence supported the decision: Regular patching occurs for major systems, but a formal risk-based vulnerability management process and SLAs are still being refined.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented. The organization should continue to refine its formal risk-based vulnerability management process and SLAs to ensure effective mitigation of risks.

#### A.8.9 - Configuration management

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: The formal scope of the ISMS, including boundaries and applicability, is defined in the separate document “Information Security Management System – Scope Statement for ABC Corporation”. | Implementing and maintaining security controls on servers, databases, networks, and supporting infrastructure.
- Evidence summary: Evidence from the scope statement and implementation status justify a Partially Implemented control.
- Gap note: No material gap is observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented as it meets the requirements of the scope statement and the formal change management process for production systems, but lacks formal configuration baselines and automated drift monitoring for all components.

#### A.8.10 - Information deletion

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Servers, network devices, storage systems, and backup media. | Documented information shall be approved prior to issue, kept up to date, protected from loss of confidentiality, integrity, or availability, and retained for as long as required by legal, regulatory, contractual, or...
- Evidence summary: Evidence supported the decision: Logical deletion processes exist in applications and databases but comprehensive retention and secure deletion rules are not yet fully implemented for all data types and environments.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented. Further implementation of logical deletion processes, including comprehensive retention and secure deletion rules, is required to ensure compliance with legal and business requirements.

#### A.8.11 - Data masking

- SoA applicable: Yes
- SoA implementation status: Not Implemented
- LLM applicability decision: Applicable
- LLM Decision: Not Implemented
- Evidence snippets: Where ABC processes personal data, including taxpayer or staff information: | ABC shall determine the needs and expectations of interested parties relevant to information security, including government tax authorities, taxpayers, employees, suppliers, regulators, and other partners.
- Evidence summary: The SoA marks the control as applicable and clearly inside scope, but there is no explicit evidence of implementation.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement data masking techniques to limit exposure of sensitive taxpayer information in non-production environments.

#### A.8.12 - Data leakage prevention

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli... | Databases and data stores holding client information.
- Evidence summary: The scope of the control is clearly defined in the SoA, and evidence supports that it is not fully implemented.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement DLP measures across all endpoints and channels to prevent data leakage.

#### A.8.13 - Information backup

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Backups of critical systems and data shall be performed regularly, stored securely, and tested for successful restore at planned intervals. | Changes to production systems shall follow a formal change management process, including assessment, approval, testing, and back‑out planning.
- Evidence summary: Evidence supported the decision: Regular backups of critical systems and data are performed, stored securely, and tested for restore.
- Gap note: No material gap observed.
- Recommendation: The control is implemented as per the SoA justification. No further action is required.

#### A.8.14 - Redundancy of information processing facilities

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli... | Where ABC uses cloud or other outsourced services, contractual clauses shall address information security requirements and responsibilities.
- Evidence summary: The SoA explicitly states that full failover for all services and locations is not yet implemented.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Implement redundancy in information processing facilities to meet availability requirements.

#### A.8.15 - Logging

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Important events such as authentication attempts, administrative actions, configuration changes, and security alerts shall be logged. | Security controls shall be selected based on ISO/IEC 27001 Annex A and other relevant standards, tailored to ABC’s context.
- Evidence summary: Evidence supported the decision: Important events such as authentication attempts, administrative actions, configuration changes, and security alerts shall be logged.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.8.16 - Monitoring activities

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: ABC shall log and monitor activities on critical systems to support detection and investigation of security events: | Management reviews shall consider the status of actions from previous reviews, changes in external and internal issues, fulfilment of information security objectives, results of monitoring and measurement, audit resul...
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Not Implemented.

#### A.8.17 - Clock synchronisation

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Any exceptions or deviations from this policy must be formally requested, assessed for risk, and approved by the Information Security Manager and appropriate management. | Approved exceptions shall be documented, time‑bound, and reviewed regularly.
- Evidence summary: Evidence supported the decision: System clocks are generally synchronised using NTP but a documented standard and monitoring for time synchronisation are still being developed.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented. The organisation should continue to monitor and develop a documented standard and monitoring for time synchronisation, as the current implementation may not be sufficient to meet business objectives.

#### A.8.18 - Use of privileged utility programs

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: User IDs shall be unique to individuals; generic and shared accounts shall be restricted and justified. | Access rights to applications, systems, and data shall be granted on a need‑to‑know and least‑privilege basis, and approved by responsible managers.
- Evidence summary: Evidence supported the decision: User IDs shall be unique to individuals; generic and shared accounts shall be restricted and justified.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, as evidenced by the existence of AccessControlPolicy.txtOperationsRunbook.txt. Further implementation is recommended to ensure compliance with ISO 27001:2022.

#### A.8.19 - Installation of software on operational systems

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Changes to production systems shall follow a formal change management process, including assessment, approval, testing, and back‑out planning. | Ensuring that changes in production environments follow approved change management procedures.
- Evidence summary: Evidence supported the decision: Changes to production systems shall follow a formal change management process, including assessment, approval, testing, and back-out planning.
- Gap note: ...
- Recommendation: The control is implemented as per the SoA justification. No material gap is observed.

#### A.8.20 - Networks security management

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Firewalls, secure configurations, and access controls shall be applied to networks under ABC control. | The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli...
- Evidence summary: The scope of the control is clearly defined in the SoA, and evidence snippets support its implementation.
- Gap note: No material gap observed.
- Recommendation: Implement firewalls routing rules and network segmentation to protect tax portals and supporting infrastructure.

#### A.8.21 - Security of network services

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: The purpose of this Information Security Management Policy is to define the principles and high‑level requirements for protecting information processed, stored, and transmitted by ABC Corporation in the course of deli... | External factors such as the legal and regulatory environment for tax administration services, contractual obligations to government clients, and the cybersecurity threat landscape.
- Evidence summary: Evidence supported the decision: SoA justification provided context for implementation status.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Not Implemented.

#### A.8.22 - Segregation of networks

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Network segmentation shall be used to separate environments (e.g., development, test, production) and protect critical systems. | Users shall not attempt to bypass security controls, install unauthorized software, or use ABC or client systems for illegal or unethical activities.
- Evidence summary: Evidence supported the decision: Network segmentation shall be used to separate environments (e.g., development, test, production) and protect critical systems.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.8.23 - Web filtering

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Access rights to applications, systems, and data shall be granted on a need‑to‑know and least‑privilege basis, and approved by responsible managers. | Company and client‑provided assets (e.g., laptops, desktops, mobile devices, network access) shall be used for authorized business purposes only.
- Evidence summary: Evidence supported the decision: Access rights to applications, systems, and data shall be granted on a need‑to‑know and least‑privilege basis, and approved by responsible managers.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.8.24 - Use of cryptography

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: ABC shall define and monitor key performance indicators and other measures needed to evaluate the effectiveness of the ISMS and the implemented controls. | Implementing and maintaining security controls on servers, databases, networks, and supporting infrastructure.
- Evidence summary: The control is clearly inside scope and marked as applicable by the SoA.
- Gap note: No material gap observed.
- Recommendation: No material gap observed.

#### A.8.25 - Secure development life cycle

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Information security requirements shall be included in contracts and agreements. | Where development or operations are outsourced, ABC shall assess and, where appropriate, monitor the supplier’s security measures.
- Evidence summary: Evidence from the SoA and mapped documents supports the implementation of secure development life cycle.
- Gap note: No material gap is observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, as it includes information security requirements in contracts and agreements. Further enhancement is recommended to formalize a secure SDLC with security checkpoints at each phase.

#### A.8.26 - Application security requirements

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Applications (taxpayer portal, department portal, main information website). | Ensuring agreed availability levels of the taxpayer and department portals, especially during statutory filing periods.
- Evidence summary: Evidence supported the decision: Applications (taxpayer portal, department portal, main information website) and Ensuring agreed availability levels of the taxpayer and department portals.
- Gap note: ...
- Recommendation: No material gap is observed. The control is implemented as per the SoA justification.

#### A.8.27 - Secure system architecture and engineering principles

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: This policy establishes the foundation of ABC’s Information Security Management System (ISMS) in alignment with ISO/IEC 27001:2022. | Apply a risk‑based approach to the selection and implementation of information security controls.
- Evidence summary: Evidence snippets support the control's implementation, but lack explicit details.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented as it establishes a foundation for ABC’s ISMS in alignment with ISO/IEC 27001:2022. Further evidence is required to demonstrate consistent enforcement of secure engineering principles across all projects.

#### A.8.28 - Secure coding

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Applying secure development practices in line with defined standards. | Development, test, and production environments shall be separated to reduce risk of unintended changes or data leakage.
- Evidence summary: Evidence supported the decision: Applying secure development practices in line with defined standards.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is partially implemented, as it applies secure coding principles to software development. Further strengthening of the formal secure coding standard and mandatory code reviews for all changes are still necessary.

#### A.8.29 - Security testing in development and acceptance

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Code changes shall undergo peer review and appropriate testing (including security testing where relevant) before deployment to production. | Root cause analysis shall be performed for significant incidents, and corrective actions implemented to prevent recurrence.
- Evidence summary: Evidence from the scope statement and SoA justification supports the implementation of security testing processes during development and acceptance phases.
- Gap note: No material gap is observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented.

#### A.8.30 - Outsourced development

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Where development or operations are outsourced, ABC shall assess and, where appropriate, monitor the supplier’s security measures. | Information security requirements shall be included in contracts and agreements.
- Evidence summary: Evidence from SoA justification and evidence snippets indicate that the control is clearly inside scope.
- Gap note: No material gap observed. Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: Not Implemented

#### A.8.31 - Separation of development test and production environments

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Development, test, and production environments shall be separated to reduce risk of unintended changes or data leakage. | Changes to production systems shall follow a formal change management process, including assessment, approval, testing, and back‑out planning.
- Evidence summary: Evidence supported the decision: Development, test, and production environments shall be separated to reduce risk of unintended changes or data leakage.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.8.32 - Change management

- SoA applicable: Yes
- SoA implementation status: Implemented
- LLM applicability decision: Applicable
- LLM Decision: Implemented
- Evidence snippets: Changes to production systems shall follow a formal change management process, including assessment, approval, testing, and back‑out planning. | Ensuring that changes in production environments follow approved change management procedures.
- Evidence summary: Evidence supported the decision: Changes to production systems shall follow a formal change management process, including assessment approval and rollback planning.
- Gap note: ...
- Recommendation: The control is Applicable. The implementation status is Implemented.

#### A.8.33 - Test information

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Access rights to applications, systems, and data shall be granted on a need‑to‑know and least‑privilege basis, and approved by responsible managers. | ABC will ensure that physical locations under its control that host or access information within the ISMS scope are appropriately protected:
- Evidence summary: Evidence supported the decision: Access rights to applications, systems, and data shall be granted on a need‑to‑know and least‑privilege basis, and approved by responsible managers.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented due to inconsistent application of least privilege and monitoring of test data use needs improvement. Further efforts are recommended to address these gaps.

#### A.8.34 - Protection of information systems during audit testing or review

- SoA applicable: Yes
- SoA implementation status: Partially Implemented
- LLM applicability decision: Applicable
- LLM Decision: Partially Implemented
- Evidence snippets: Changes to production systems shall follow a formal change management process, including assessment, approval, testing, and back‑out planning. | Ensuring agreed availability levels of the taxpayer and department portals, especially during statutory filing periods.
- Evidence summary: Evidence supported the decision: Changes to production systems follow a formal change management process, and ensuring agreed availability levels of taxpayer and department portals is clearly stated in the SoA.
- Gap note: ... Adjusted applicability to Applicable because the SoA marks this control as applicable and no strong scope-based exclusion was established.
- Recommendation: The control is Partially Implemented due to the lack of explicit guidance on standard procedures for test tools and access during audits. Further clarification from the SoA is required to upgrade the implementation status.
