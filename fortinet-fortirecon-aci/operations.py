""" Copyright start
  Copyright (C) 2008 - 2024 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """


from .get_iocs import get_iocs
from .get_leaked_cards import get_leaked_cards
from .get_widgets import get_widgets
from .get_osint_feeds import get_osint_feeds
from .get_reports import get_reports
from .get_reports_with_iocs import get_reports_with_iocs
from .get_stealers_log import get_stealers_log
from .get_icl_saved_searches import get_icl_saved_searches
from .get_icl_saved_searches_by_id import get_icl_saved_searches_by_id
from .get_ransomware_information import get_ransomware_information
from .get_stealers_infections_leaked_count import get_stealers_infections_leaked_count
from .get_leaked_stealers_infections import get_leaked_stealers_infections
from .get_vendor_details_by_id import get_vendor_details_by_id
from .get_vendor_watchlist import get_vendor_watchlist
from .get_vulnerability_intelligence_cves import get_vulnerability_intelligence_cves
from .get_vulnerability_intelligence_cves_by_id import get_vulnerability_intelligence_cves_by_id
from .get_vulnerability_intelligence_elevated_cves import get_vulnerability_intelligence_elevated_cves
from .get_vulnerability_intelligence_global_cves import get_vulnerability_intelligence_global_cves
from .get_vulnerability_intelligence_global_cves_by_id import get_vulnerability_intelligence_global_cves_by_id
from .get_vulnerability_intelligence_information import get_vulnerability_intelligence_information


operations = {
    "get_iocs": get_iocs,
    "get_leaked_cards": get_leaked_cards,
    "get_widgets": get_widgets,
    "get_osint_feeds": get_osint_feeds,
    "get_reports": get_reports,
    "get_reports_with_iocs": get_reports_with_iocs,
    "get_stealers_log": get_stealers_log,
    "get_icl_saved_searches": get_icl_saved_searches,
    "get_icl_saved_searches_by_id": get_icl_saved_searches_by_id,
    "get_ransomware_information": get_ransomware_information,
    "get_stealers_infections_count": get_stealers_infections_leaked_count,
    "get_leaked_stealers_infections": get_leaked_stealers_infections,
    "get_vendor_details_by_id": get_vendor_details_by_id,
    "get_vendor_watchlist": get_vendor_watchlist,
    "get_vulnerability_intelligence_cves": get_vulnerability_intelligence_cves,
    "get_vulnerability_intelligence_cves_by_id": get_vulnerability_intelligence_cves_by_id,
    "get_vulnerability_intelligence_elevated_cves": get_vulnerability_intelligence_elevated_cves,
    "get_vulnerability_intelligence_global_cves": get_vulnerability_intelligence_global_cves,
    "get_vulnerability_intelligence_global_cves_by_id": get_vulnerability_intelligence_global_cves_by_id,
    "get_vulnerability_intelligence_information": get_vulnerability_intelligence_information
}
