#pragma once
#include <cstdint>
#include <functional>
#include <string>

namespace chm::net {
enum class Mode { Offline, Client, Server, Host, P2P, Hybrid };
struct Profile { std::string nickname; std::string avatar_ref; };
struct Config { Mode mode{Mode::Offline}; std::string host{"127.0.0.1"}; std::uint16_t port{45678}; std::string application_id{"general-app"}; std::string room{"main"}; Profile profile{}; bool enable_p2p{true}; bool tls{true}; };
struct Envelope { std::uint32_t version{1}; std::string type; std::string id; std::string room; std::string sender; std::uint64_t timestamp_ms{}; std::string payload_json; };

class Transport {
public:
  virtual ~Transport() = default;
  virtual bool start(const Config&) = 0;
  virtual void stop() = 0;
  virtual bool send(const Envelope&) = 0;
  virtual bool running() const = 0;
};

// Host implementations should instantiate server and local-client transports and route
// local messages through the same authorization/event path used by remote clients.
class SessionController {
public:
  virtual ~SessionController() = default;
  virtual bool start(const Config&) = 0;
  virtual void stop() = 0;
};
} // namespace chm::net
