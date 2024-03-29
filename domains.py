domain_to_section = {
    "Matematyka": [
        "Logarytmy i Potęgi 1",
        "Podstawowe operacje matematyczne 1",
        "Operacje na ułamkach 1",
        "Równania i nierówności 3",
    ]
}

section_to_domain = dict((section, domain) for domain, sections in domain_to_section.items() for section in sections)
