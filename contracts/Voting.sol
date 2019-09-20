pragma solidity >=0.5.0 <0.6.0;


contract Voting {
    struct Candidate {
        string name;
    }

    Candidate[] public candidateList;

    mapping (uint => address) public candidateToOwner;
    mapping (address => uint) votesReceived;

    function add_candidate(string memory _name) public{
        Candidate memory newCandidate = Candidate(_name);
        uint candidateId = candidateList.push(newCandidate) - 1;
        candidateToOwner[candidateId] = msg.sender;
    }

    function get_number_of_candidates() external view returns(uint) {
        return candidateList.length;
    }

    function get_candidate_info(uint _candidateId) external view returns (address, string memory, uint) {}
    function totalVotesFor(uint _candidateId) public view returns (uint256) {
        require(
            validCandidate(_candidateId),
            "error msg"
        );
        return votesReceived[candidateToOwner[_candidateId]];
    }
    function voteForCandidate(uint _candidateId) public {
        require(
            validCandidate(_candidateId),
            "error msg"
        );
        votesReceived[candidateToOwner[_candidateId]] += 1;
    }
    function validCandidate(uint _candidateId) public view returns (bool) {
        if (_candidateId < candidateList.length) {
            return true;
        }
        return false;
    }
}