#pragma once
#include <string>
#include <vector>
struct PeerEnvelope { std::string peer_id; std::string event_id; uint64_t sequence{}; std::string timestamp; std::string payload_hash; std::string signature; };
struct VerificationResult { bool accepted; std::string reason; };
class PeerProtocol { public: VerificationResult verify(const PeerEnvelope& e,const std::string& expected_peer,uint64_t expected_sequence) const; };