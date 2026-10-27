# booking_rules.py

class JohannesburgRule:

    @staticmethod
    def validate(duration, hour):

        if duration > 4:
            return (
                False,
                "Maximum booking duration is 4 hours."
            )

        return True, ""


class PretoriaRule:

    @staticmethod
    def validate(duration, hour):

        if hour < 8 or hour > 17:

            return (
                False,
                "Bookings are only allowed between 08:00 and 17:00."
            )

        return True, ""


class CapeTownRule:

    @staticmethod
    def validate(duration, hour):

        if duration > 2:

            return (
                False,
                "Maximum booking duration is 2 hours."
            )

        return True, ""


rules = {
    "Johannesburg": JohannesburgRule,
    "Pretoria": PretoriaRule,
    "Cape Town": CapeTownRule
}