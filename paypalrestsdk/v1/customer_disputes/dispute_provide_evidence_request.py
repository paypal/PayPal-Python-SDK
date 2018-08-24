# This class was generated on Sun, 08 Apr 2018 16:12:12 UTC by version 0.1.0-dev+291f3f of Braintree SDK Generator
# dispute_provide_evidence_request.py
# @version 0.1.0-dev+291f3f
# @type request
# @data H4sIAAAAAAAC/7xW33Pbtg9///4VOH730NzJlrutXec3t3ESd2ni2e52uywX0xJs8UKRKkEm9Xr533cQpdiO03Y/cnvxWSDwAT4ACPCTOJMlir7IFVXBY7dy9kbl2EH+NRmKRBwiZU5VXlkj+mIcFQhaDVhaBxIagAQWaxgddmEAJbqskMZDJg00uLtWjQ3BrfIF+ALh99DrfZdlNsf6H/46GM1GZ8dXR+eTq+nw9HQ4uZoMp+Pzs+kwqqYbXSAvfSC4LZRGyAJ5W6Kjp3L/+v1vf8F7F4atC/a7QJDs3C7BLiFHrW7QrcG6jdDhMpgccpuFEo3nM2M9UsJEsqKGUSbTIUfQdkWc2n3Ee/NGlUCCdzK7VmYFJpQLdE1i5Oddb9k2R1zJWcHp0treMpYLmhWqSq/B243tkrH9uuJDkwOpP5D6MUtBxxTFL63iF8MSao2uphgqbWUOoWLU5z1495ojZFRqOiyThN0m7y3ILuTI5OpG5UHqxrAM5LkGVMrakS+kgRfw7vWXcerQQlVZ5zGPzJbWldITSIfwdnycwPHoKIHx2XFS0x0fHj0Ome6SX7i0cWGhlNcIvlAEDj8EJJ8AVZip5bruxaY7YXQIytSS95NRzO2W1n1DNzpvp+dnLR4sbL7uikT8HNCtx9LJEj06Ev2Ly0ScoMzRPZQeWVfuyD6J2briCcFpEIn4RTolFxqbubE1J37CdSPcGxqDmMT6nrUWHNjAObmO+L1ETFDm50avRX8pNSELPgTlMBd97wImPHsqdF4hib4JWt9dJmIsffF4wOSdMqv9kJvEXqn8y0FzF4wOuQu3y8G9GC+mt0BhUSr/1JQmsXwRhIUsosoawii7pzgNC2Jl42GQcdi0T/fLJLcQZET4WyQawTaLTQFOlbmGbXd7sWllrmknwFbyoH8MSA4pDq06Ox2HWvL1vDgZzIbngynUppfP0txmlMpKpYX0aCV16oP04AGxl/+c2Oc6q3C43GHTCPb7KrNlpdEjeOlW6OH95LQLm5mA0LLLpNYJqy+UiScl+sLm7c5SBBc8F2ZYVmzRiYPKY375rPC+on6aems1dRX6Zde6VVr4Uqdumb188UPvoM5aF47qjYSdytkMiZRZJfdLh53Ov5knMH82j9NufjCHrJBOZnzn4oaYM9c5KKr1r3ENbV2YqzXcYb6QPpaJx3mTgsgx8pF8o9p+ZPG/bcb6SiVfLVzM6U7p7kX7xTuZzcZtGVzjnafBo8X7jxg41Dvhx+/92C84/TFAZU29sL/aKC9+fPXq/4T1eOh8f9A+TAjdDW97Xvg8KOOWrvHrQgcjy4VaBRtIryGvQ1lg7A/CUhqvMmrHa2zDKSJc1GNj0kRIm+hub2+7ShpZxyaJ1Mrwy4NStu20lB5+dj8yjYMnKcPl3eVdIt5Y49E041mUQXtVSefTpuoiESfeV+9i//TF+Hw6E3FPib5Ib56n7dM0bR+g6afNTrpLH3mCT69VdR/W8GOFmcd8Wj8439gcRf/bXu/uf38CAAD//w==
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class DisputeProvideEvidenceRequest:
    """
    Provides evidence for a dispute, by ID. A merchant can provide evidence for disputes with the <code>WAITING_FOR_SELLER_RESPONSE</code> status while customers can provide evidence for disputes with the <code>WAITING_FOR_BUYER_RESPONSE</code> status. Evidence can be a proof of delivery or proof of refund document or notes, which can include logs. A proof of delivery document includes a tracking number while a proof of refund document includes a refund ID. The following rules apply to document file types and sizes:<ul><li>The seller can upload up to 10 MB of files for a case.</li><li>Individual files must be smaller than 5 MB.</li><li>The supported file formats are JPG, GIF, PNG, and PDF.</li></ul><br/>To make this request, specify the dispute ID in the URI and specify the evidence in the JSON request body.
    """
    def __init__(self, dispute_id):
        self.verb = "POST"
        self.path = "/v1/customer/disputes/{dispute_id}/provide-evidence?".replace("{dispute_id}", quote(str(dispute_id)))
        self.headers = {}
        self.headers["Content-Type"] = "multipart/form-data"
        self.body = None

    def request_body(self, body):
        self.body = body
        return self
    
