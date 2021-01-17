---
layout: post
title: 'Cybersecurity: Hardening C-Based Toolchain'
tags:
- development
- cybersecurity
- best-practice
---

When developing medical device products, one of the major milestones is to obtain the US Food and Drug Administration (FDA) clearance of a new Premarket Notification, a.k.a., PMN or 510(k). &nbsp;For those who are not familiar with it, FDA requires medical device manufacturers to register and notify FDA of their intent to market a medical device at least 90 days in advance. &nbsp;A 510(k) is the technical dossier where the manufacturers must provide FDA with evidence that the product has been developed with _proper_ processes in place and thus is safely and effectively used and distributed as medical devices.

FDA recently released a draft guidance for its recommendations to industry regarding management of cybersecurity in medical devices (October 18th, 2018; See [here](https://www.fda.gov/MedicalDevices/DigitalHealth/ucm373213) for further details). &nbsp;This cybersecurity involves many different aspects of the medical device systems, including hardware, software, processes, usability, and so on. &nbsp;In terms of software, one approach to enhancing cybersecurity (among many others) is to tighten up built binaries in order to minimize potential risks of the binaries being exploited by malicious attacks such as stack smashing. &nbsp;This can be done by setting some compiler and linker flags. &nbsp;For example, below is a CMake code snippet that I wrote to bring in some of the security flags into the build chain of our system:

    set (SECURITY_NO_PIE_CFLAGS -fstack-protector-strong -D_FORTIFY_SOURCE=2)
    set (SECURITY_CFLAGS_PIE -fPIE)
    set (SECURITY_CFLAGS_WARN -Wformat=2 -Wformat-security -Wstrict-overflow)
    set (SECURITY_CFLAGS_ALL ${SECURITY_NO_PIE_CFLAGS}
                             ${SECURITY_CFLAGS_PIE}
                             ${SECURITY_CFLAGS_WARN})
    
    set (SECURITY_LDFLAGS_RELROPARTIAL -Wl,-z,relro)
    set (SECURITY_LDFLAGS_RELROFULL -Wl,-z,relro,-z,now)
    set (SECURITY_LDFLAGS_PIE -pie -fPIE)
    set (SECURITY_LDFLAGS_ALL ${SECURITY_LDFLAGS_PIE}
                              ${SECURITY_LDFLAGS_RELROFULL})
    
    string (REPLACE ";" " " SECURITY_CFLAGS_ALL "${SECURITY_CFLAGS_ALL}")
    string (REPLACE ";" " " SECURITY_LDFLAGS_ALL "${SECURITY_LDFLAGS_ALL}")
    
    set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${SECURITY_CFLAGS_ALL} ${SECURITY_LDFLAGS_ALL}")
    set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${SECURITY_CFLAGS_ALL} ${SECURITY_LDFLAGS_ALL}")

Looking at those flags, I was curious about, what are those flags, how do they work, and why this particular combination of flags? &nbsp;It turns out, with a bit of googling, there is a body of work called the **[C-Based Toolchain Hardening](https://www.owasp.org/index.php/C-Based_Toolchain_Hardening)**. &nbsp;From the website:

> C-Based Toolchain Hardening is a treatment of project settings that will help you deliver reliable and secure code when using C, C++ and Objective C languages in a number of development environments.

Behind this effort is the [**OWASP Foundation**](https://www.owasp.org), the free and open software security community. &nbsp;Among [their github repos](https://github.com/OWASP), there is one interesting project called the **OWASP Cheat Sheet Series** ([project website](https://www.owasp.org/index.php/OWASP_Cheat_Sheet_Series), [github repo](https://github.com/OWASP/CheatSheetSeries)). &nbsp;Essentially, it is a collection of guidelines and best practices around application security topics. &nbsp;Here are some cheat sheets from the collection that seem interesting:

- [C-based toolchain hardening](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/C-Based_Toolchain_Hardening.md)
- [C-based toolchain hardening cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/C-Based_Toolchain_Hardening_Cheat_Sheet.md)
- [Threat modeling cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Threat_Modeling_Cheat_Sheet.md)
- [Access control cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Access_Control_Cheat_Sheet.md)
- [Authentication cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Authentication_Cheat_Sheet.md)
- [Logging cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Logging_Cheat_Sheet.md)
- [Key management cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Key_Management_Cheat_Sheet.md)
- [Ruby on rails cheat sheet](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Ruby_on_Rails_Cheatsheet.md)

CONTINUE HERE...

four areas to be examined when hardening the toolchain: configuration, preprocessor, compiler, and linker

1. Configuration
2. Preprocessor
3. Compiler
4. Linker

## Further Readings

### Cybersecurity

- FDA Cybersecurity: [https://www.fda.gov/MedicalDevices/DigitalHealth/ucm373213](https://www.fda.gov/MedicalDevices/DigitalHealth/ucm373213)
- NIST Cybersecurity Framework: [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework)

### Security Hardening

- C-Based Toolchain Hardening: [https://www.owasp.org/index.php/C-Based\_Toolchain\_Hardening](https://www.owasp.org/index.php/C-Based_Toolchain_Hardening)
- 
- [Secure Programming HOWTO - Creating Secure Software](https://dwheeler.com/secure-programs/)
- Hardening: [https://wiki.debian.org/Hardening](https://wiki.debian.org/Hardening)
- Clang hardening cheat sheet: [https://blog.quarkslab.com/clang-hardening-cheat-sheet.html](https://blog.quarkslab.com/clang-hardening-cheat-sheet.html)
- Stackoverflow: [https://security.stackexchange.com/questions/24444/what-is-the-most-hardened-set-of-options-for-gcc-compiling-c-c](https://security.stackexchange.com/questions/24444/what-is-the-most-hardened-set-of-options-for-gcc-compiling-c-c)
- Visual C++ security features: [https://docs.microsoft.com/en-us/cpp/security/security-best-practices-for-cpp?view=vs-2017](https://docs.microsoft.com/en-us/cpp/security/security-best-practices-for-cpp?view=vs-2017)
- RED HAT Developer: Recommended compiler and linker flags for gcc: [https://developers.redhat.com/blog/2018/03/21/compiler-and-linker-flags-gcc/](https://developers.redhat.com/blog/2018/03/21/compiler-and-linker-flags-gcc/)
