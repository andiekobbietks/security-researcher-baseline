[ ![Cobalt](https://www.cobalt.io/hubfs/assets/images/logos/cobalt-logo-color-no-TM.svg)](https://www.cobalt.io/)

- Platform

- Services

- Solutions

- Resources

- About

[](https://app.cobalt.io/) [ Request a Demo](https://www.cobalt.io/get-started)

# How to Write a Great Vulnerability Assessment Report with this Template

David Sopas shares his advice on writing a high-quality vulnerability assessment report.

Sep 28, 2016

Est Read Time: 7 min

![](https://www.cobalt.io/hubfs/Imported%20images/David.jpeg%3Ffit=scale%26w=130%26q=90%26fm=webp.jpeg)

[David Sopas](https://www.cobalt.io/blog/author/david-sopas)

- [](https://www.facebook.com/sharer.php?u=https://www.cobalt.io/blog/how-to-write-a-great-vulnerability-report)

- [ ](https://linkedin.com/shareArticle?mini=true&title=How+to+Write+a+Great+Vulnerability+Assessment+Report+with+this+Template&url=https://www.cobalt.io/blog/how-to-write-a-great-vulnerability-report)

- [](https://twitter.com/share?text=How+to+Write+a+Great+Vulnerability+Assessment+Report+with+this+Template&url=https://www.cobalt.io/blog/how-to-write-a-great-vulnerability-report)

David Sopas is a longtime member of the Cobalt Core and the no. 1 ranked researcher on the Cobalt Hall of Fame. He also leads up [Char49](https://char49.com/) and works as a consultant in Checkmarx. David has found [several critical vulnerabilities](/blog/adding-clarity-in-the-murky-world-of-vulnerability-risk) in top sites and is always looking for a new challenge. Among other achievements he recently was the first to reach 2,000 rep points on Cobalt, but his work is not over yet. In this blog post he shares his advice on writing a high-quality vulnerability assessment report.

## Introduction to Vulnerability Report

Based on my experience with bug bounties and penetration tests (pentests) on Cobalt.io and other platforms, I have learned that a well written report of bugs or pentests will make a major difference in your ability to help the program owners or pentest clients understand and correct problems and increase your value.

In the world of vulnerability reporting, you sometimes come across the following type of vulnerability reports:

*“You guys don’t have an SPF header on your mail server. Check it online here: http://relevant”*

Or even begging for a better reward:

*“Mr. \[Relevant\] received $100 for this report. Can you please pay $50 more? Please? I deserve more!”*

If I was a bug bounty program owner (or program curator) or pentest client, I would categorize both reports with 'WTF' — not based on the vulnerability itself, but the lack of information and effort by the security researcher or white hat hacker. Don’t forget you need to sell your service. You need to show the program owners or clients that you care about their security and that you can talk the talk — *articulating the problem* in clear terms and demonstrating some authority on the subject.

In this blog post, I will share some of my own best practices for writing great security vulnerability assessment reports for bug bounty programs and penetration tests. A good vulnerability assessment report aims to provide network security engineers insights into system vulnerabilities with an end goal of empowering the remediation process, understanding the risk they present, and the potential for a network breach.

You can use this information to create a template for vulnerability or pentest findings — whether you want to call that a vulnerability assessment report template, sample vulnerability assessment report, vulnerability scan report template, vulnerability assessment template, security vulnerability assessment template, or a penetration testing report template. The principles are the same.

## 1\. Prepare before you test

Being professional and understanding what the business is looking for often makes the difference between earning a few bucks and hitting a homerun.

To start, carefully read the program or project scope and rules of engagement. This is one of the most important things to do before you begin researching and testing.

***Bug Bounty Preparation*** — Imagine spending time finding a security bug and writing an awesome bug report and then, in the end, the program owners tells you it’s out of scope — it’s frustrating. It happened to me when I first started working on bug bounty programs. I didn’t spend enough time reading the program scope. If you have specific questions about the scope, contact the program owners/curators by email or use the comments on another report you are submitting to contact them.

[Rules of engagement for bug bounty programs](https://fc18.ifca.ai/preproceedings/105.pdf) provide details such as:

- In-scope areas

- Out-of-scope areas

- Out-of-scope techniques and methods such as social engineering or use of automated scanning tools

- Vulnerability types that are eligible for the program

- Vulnerability types that are ineligible

- Program-specific instructions such as setting up a test account and submitting a bug

- Terms

- Restrictions based on researcher age, location, or other factors

- Guidelines for public disclosure

- Reward eligibility criteria including reward rules for duplicate reports

***Pentest Preparation*** — For pentests, service agreements and statements of work include similar information about the scope including a list of the in-scope components of the network, web or mobile application, system, API, or other asset. The security researcher does not publicly disclose pentest vulnerabilities (vulns) unless contractually permitted to do so.

## 2\. Writing a good report

After you have done some research and found a great vulnerability, the next step is to make a good report of your findings. Whether you are communicating a security weakness in a bug bounty submission or a penetration testing report, the basics of what you include are the same.

To help you guys out, I have explained some of the guidelines I use to write good reports. I have explained it according to the format found on the [Cobalt platform](/platform) — a structure which could also be replicated in an email or a free-text report.

### Title of the vulnerability

When creating a title for the vulnerability, be explicit about what the vulnerability is. Don’t write show-off titles. Let’s consider an cross-site scripting example (XSS vulnerability example):

Example of a good title — *Reflected XSS on reference parameter at product page*

Example of a bad title — *CRITICAL — XSS on your program*

Keep in mind that this is the first thing the program owners or clients will see. It’s their first impression of you and your report.

### Description

A vulnerability description must be short, clear, and direct. Program owners and clients don’t want to spend much time reading.

A great way to describe a vulnerability in a short, clear way is to include references/links to trusted sources that can help others understand, identify, and fix the bug. This could be an OWASP link, CVE references or links to other public advisories and standards. (Don’t reference Wikipedia or other less respected sites.)

e.g. If I find a XSS bug, I’ll explain what it is, give an OWASP reference, tell them what type of XSS was found, and so on.

Don’t copy-paste information from automated tools or other sources into the description. It shows the program owners or clients that you didn’t even take the time to write a few words specific to their scenario.

If it is my first time submitting a report to a bounty program, I’ll introduce myself and say “hello.” There’s nothing wrong with showing a little politeness.

### Proof-of-concept

In the proof-of-concept section, I always treat program owners and clients as if they are newbies. I provide a clear step-by-step guide or process showing how to replicate the vulnerability.

Example of a XSS proof of concept:

**Step 1:** Go to the following \[URL\]

**Step 2:** Enter your username and password (you need an account to do this)

**Step 3:** In the Search box at top right, insert the following information:

\<script\>alert(document.domain);\</script\>

**Step 4:** Click the “Search” button

**Step 5:** You’ll see a JavaScript popup box showing your domain

Check the attached screenshot to see the actual XSS vulnerability.

Depending on the type of vulnerability, I may also show the reflected code so the program owners and clients can identify faster where the payload is loading. Example:

![great report 2](https://www.cobalt.io/hs-fs/hubfs/Imported_Blog_Media/great_report_2-1.png?width=680&name=great_report_2-1.png)

### Criticality Assessment

To give the program owners and clients an idea of the seriousness or criticality of a security weakness, you can explain how a malicious user or black hat hacker could attack by exploiting the vulnerability you found. Describe how and what the company (and its clients and customers) can lose with this vulnerability, in particular the impact on confidentiality, integrity, and availability. The criticality assessment could consider factors such as customer privacy, reputation impact for the company, inappropriate access to proprietary or confidential data such as intellectual property or marketing plans, potential regulatory fines, or compliance risks.

You might also be called upon to assign a criticality rating. In the Cobalt.io platform, the rating is based on impact and business context such as the damage potential, reproducibility, exploitability, number of affected users, and discoverability of each finding.

## 3\. Tools

Share which tool or tools you used when finding the vulnerability. If you used only a browser, identify the required browser version. For particular types of vulns, the proof of concept will only work on some versions so be specific.

Example: Burp, Nmap and Firefox 47\.0

## 4\. Attachments

Provide screenshots, video, or audio recording to improve and add value to your report.

Sometimes program owners and clients can’t replicate the vulnerability so helping them with images or a step-by-step video or audio will help them significantly.

If you can’t do a video, just send an audio version explaining how to replicate your finding. This will also show the owners and clients that you took time to create a good report and they may even evaluate you a little higher for the extra effort.

## 5\. Suggested Fixes/Solutions

Show the program owners clear solutions for their problem. Give examples, don’t just tell them to sanitize the input, but also give them references and possible ways to do it. They’ll greatly appreciate it. Sometimes the developers don’t know how to fix a vulnerability, and if you provide a great description of a suggested fix it’s a win-win situation. After all, the key mission is to fix the vulnerabilities.

### Comments

Comments are great when/if the program owners or clients need further clarification on the report.

Always be polite and, for bounty programs, don’t continually ask for updates. You can ask owners once or twice every month, and if you are not getting any feedback, contact the platform support team to help moderate the issue.

### Differences Between Bug Bounty Reports and Pentest Reports

A bug bounty report documents a single vulnerability while a pentest report documents all discovered vulnerabilities. For instance, an average application pentest discovers 20 to 30 vulnerabilities.

#### Pentest Executive Summary

Pentest reports typically include an Executive Summary near the beginning to provide a testing overview and the security tester’s impression of overall security risk. The Executive Summary also notes any trends in the types of weaknesses found; for instance, if several weaknesses fall under an OWASP Top 10 category, it would be noted. The Summary also could include information from the project’s Statement of Work such as [assessment scope](/blog/how-to-scope-a-network-pentest-tips-from-an-expert-pentester) and methodologies. Ideally, the Summary is written in less technical terms to encourage distribution beyond the IT and security teams to business and [management stakeholders](/blog/how-to-communicate-the-business-impact-of-vulnerabilities). After all, security risk is ultimately business risk. The Summary also typically includes a list or table of discovered vulns.

#### Interactive Pentest Reports

Historically, pentest reports are delivered at the end of an engagement in a linear PDF, but the[ age of the interactive pentest report is dawning](/blog/4-tips-for-making-the-most-of-a-pen-test-report). Organizations like Cobalt.io are leading the way in providing a real-time dashboard and detail views so clients can track progress throughout an engagement. This creates efficiency while also increasing the level of communication with the client. For instance, the development team, security engineers, or others responsible for fixing open issues can ask questions and learn from the researcher during testing. In addition, the client can mark a vulnerability ready for retest, allowing you to immediately proceed with retest and close the bug as resolved.

## Conclusion

The main goal in producing a quality report is to show program owners and clients that you are there to help — collaboratively working with them, unified against the bad guys. The problem is that sometimes that connection is not clearly established. By being professional and writing great reports, you can build a stronger relationship with the companies you assist, making you the resource of choice for future programs and assessments.

I hope this blog post will help improve your reports, and benefit the organizations you assist along the way. Read more about how Cobalt offers a variety of reports including [attestation letters to prove you've completed a pentest successfully](/blog/cobalt-platform-deep-dive-attestation-letters).

Cya next time!

[![State of Pentesting Report 2026 Call to Action](https://no-cache.hubspot.com/cta/default/2689945/57a55919-c8bd-49c1-bde9-0b8d165c5e79.png)](https://cta-redirect.hubspot.com/cta/redirect/2689945/57a55919-c8bd-49c1-bde9-0b8d165c5e79)

[Back to Blog](/blog)

![](https://www.cobalt.io/hubfs/Imported%20images/David.jpeg%3Ffit=scale%26w=130%26q=90%26fm=webp.jpeg)

##### About David Sopas

David is a security researcher with more than 15 years of experience in penetration testing and vulnerability research. In the past, he's been acknowledged by companies like Microsoft, Google, Yahoo!, Adobe, and many others. David is passionate to share knowledge and inspire other people and a regular speaker at BSides and had the honor to speak at DEF CON. [More By David Sopas](https://www.cobalt.io/blog/author/david-sopas)

#### Related readings

[ ![](https://www.cobalt.io/hubfs/Imported_Blog_Media/How_to_Evaluate_Vulnerability_Reports-2.png)](https://www.cobalt.io/blog/how-to-evaluate-vulnerability-reports)

##### [ How to Evaluate Vulnerability Reports](https://www.cobalt.io/blog/how-to-evaluate-vulnerability-reports)

[Thought Leadership](https://www.cobalt.io/blog/tag/thought-leadership)

Blog

Mar 18, 2014

[ Read more](https://www.cobalt.io/blog/how-to-evaluate-vulnerability-reports)

[ ![](https://www.cobalt.io/hubfs/Imported_Blog_Media/How_Pentest_as_a_Service_Benefits_Developers_for_Vulnerability_Remediation-1.webp)](https://www.cobalt.io/blog/pentest-as-a-service-benefits-developers)

##### [ How Pentest as a Service Benefits Developers for Vulnerability Remediation](https://www.cobalt.io/blog/pentest-as-a-service-benefits-developers)

[Thought Leadership](https://www.cobalt.io/blog/tag/thought-leadership)

Blog

Aug 6, 2021

[ Read more](https://www.cobalt.io/blog/pentest-as-a-service-benefits-developers)

[ ![](https://www.cobalt.io/hubfs/Imported_Blog_Media/Screen_Shot_2021-11-02_at_9_50_23_AM-1.png)](https://www.cobalt.io/blog/adding-clarity-in-the-murky-world-of-vulnerability-risk)

##### [ Adding clarity in the murky world of vulnerability risk](https://www.cobalt.io/blog/adding-clarity-in-the-murky-world-of-vulnerability-risk)

[Product Innovation](https://www.cobalt.io/blog/tag/product-innovation)

Blog

Oct 31, 2021

[ Read more](https://www.cobalt.io/blog/adding-clarity-in-the-murky-world-of-vulnerability-risk)

[ see more](/blog)

### Never miss a story

**Stay updated about Cobalt news as it happens**

###

![](https://www.cobalt.io/hubfs/assets/images/logos/cobalt-logo-reversed-tight.svg)

###### Get Started

- [Pricing](https://www.cobalt.io/pricing)

- [Demo Center](https://www.cobalt.io/demo-center)

- [Request a Quote](https://www.cobalt.io/get-started-quote)

###### Platform

- [Platform](https://www.cobalt.io/platform)

- [Artificial Intelligence](https://www.cobalt.io/platform/artificial-intelligence)

- [PTaaS](https://www.cobalt.io/platform/ptaas)

- [DAST](https://www.cobalt.io/platform/dast)

- [Integrations](https://www.cobalt.io/platform/integrations)

###### Services

- [Penetration Testing](https://www.cobalt.io/services#security)

- [Application Security](https://www.cobalt.io/services/application-security)

- [Network Security](https://www.cobalt.io/services/network-cloud-security)

- [Additional Services](https://www.cobalt.io/services#security)

- [All Services](https://www.cobalt.io/services)

###### Solutions

- [Enterprise](https://www.cobalt.io/solutions/enterprise)

- [SMB](https://www.cobalt.io/solutions/pentest-security-platform)

- [Compliance](https://www.cobalt.io/solutions/compliance)

- [Secure SDLC](https://www.cobalt.io/solutions/secure-sdlc)

###### Cobalt Comparisons

- [Traditional Pentesting](https://www.cobalt.io/solutions/cobalt-vs-traditional-pentesting-providers)

- [Bug Bounties](https://www.cobalt.io/solutions/cobalt-vs-bug-bounty-providers)

- [Automated Pentesting](https://www.cobalt.io/solutions/cobalt-vs-autonomous-pentesting-providers)

- [Compliance-Only Pentesting](https://www.cobalt.io/solutions/cobalt-vs-compliance-only-pentesting-providers)

###### Helpful Links

- [Customer Login](https://app.cobalt.io)

- [Product Documentation](https://docs.cobalt.io/)

- [Resources](https://www.cobalt.io/resources)

- [Blogs](https://www.cobalt.io/blog)

- [Events and Webinars](https://www.cobalt.io/events)

- [Learning Center](https://www.cobalt.io/learning-center)

- [Trust Center](https://www.cobalt.io/trust-center)

- [Careers](https://www.cobalt.io/life)

[![](https://www.cobalt.io/hubfs/assets/images/logos/social-icons/icons-facebook.svg)](https://www.facebook.com/people/Cobaltio/61561052005386/) [![](https://www.cobalt.io/hubfs/assets/images/logos/social-icons/icons-X.svg)](https://twitter.com/cobalt_io) [![](https://www.cobalt.io/hubfs/assets/images/logos/social-icons/icons-linkedin.svg)](https://www.linkedin.com/company/cobalt_io) [![](https://www.cobalt.io/hubfs/assets/images/logos/social-icons/icons-youtube.svg)](https://www.youtube.com/channel/UCsWLzFUqOmAmjfP_CKMnO3g)

© 2026 Cobalt Labs, Inc. All rights reserved. [Terms of Use and Privacy](https://www.cobalt.io/terms) [Your Privacy Settings](#) [Sitemap](https://www.cobalt.io/sitemap)