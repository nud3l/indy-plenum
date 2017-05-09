def test_node_uses_own_last_ordered_no_to_nominate():
    """
    A node that receives a Nomination from other but responds with own
    last ordered no. Other nodes which do not get nomination in time Nominate
    themselves with their last ordered no
    """
    # TODO
    pass


def test_node_nominates_with_acceptable_last_ordered():
    """
    Acceptable last ordered seqno is defined as the one for which there
    are greater than f nominations and there are less than or equal to f higher
    nominations. Returns None if cannot find such a number.
    """
    # TODO
    pass


def test_all_nodes_agree_on_single_state_for_new_view():
    """
    Node which is slow in processing COMMITs agree to the same state as others
    during the election
    """
    # TODO
    pass


def test_nodes_send_re_election_when_no_acceptable_state():
    # TODO
    pass
