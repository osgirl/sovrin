import pytest
from plenum.common.txn import TYPE, NONCE

from plenum.common.types import f
from plenum.test.eventually import eventually
from sovrin.agent.agent import WalletedAgent
from sovrin.test.agent.conftest import checkAcceptInvitation

from sovrin.test.agent.helper import ensureAgentsConnected


def testFaberCreateLink(faberLinkAdded):
    pass


def testAliceLoadsFaberInvitation(aliceFaberInvitationLoaded):
    pass


def testAliceSyncsFaberInvitationLink(aliceFaberInvitationLinkSynced):
    pass


def testAliceAgentConnected(faberAdded, aliceAgentConnected):
    pass


def testFaberAdded(faberAdded):
    pass


def testAliceAcceptFaberInvitation(aliceAcceptedFaber):
    pass


def testAliceAcceptAcmeInvitation(aliceAcceptedAcme):
    pass


@pytest.mark.skip("Not yet implemented")
def testAddClaimDef():
    raise NotImplementedError


@pytest.mark.skip("Not yet implemented")
def testAddIssuerKeys():
    raise NotImplementedError


def testMultipleAcceptance(aliceAcceptedFaber,
                           faberIsRunning,
                           faberLinkAdded,
                           faberAdded,
                           walletBuilder,
                           agentBuilder,
                           emptyLooper,
                           faberNonceForAlice):
    """
    For the test agent, Faber. Any invite nonce is acceptable.
    """
    faberAgent, _ = faberIsRunning
    assert len(faberAgent.wallet._links) == 1
    link = next(faberAgent.wallet._links.values())
    wallet = walletBuilder("Bob")
    otherAgent = agentBuilder(wallet)
    emptyLooper.add(otherAgent)

    checkAcceptInvitation(emptyLooper,
                          nonce=faberNonceForAlice,
                          userAgent=otherAgent,
                          agentIsRunning=faberIsRunning, linkName=link.name)

    assert len(faberAgent.wallet._links) == 2

