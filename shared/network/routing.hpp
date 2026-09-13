#pragma once
#include <cstdint>
#include <string>
#include <vector>
#include <optional>
#include <algorithm>
#include <utility>

namespace chm::routing {
enum class AddressFamily { IPv4, IPv6, DualStack };
enum class Protocol { Static, Connected, RIP, RIPng, OSPFv2, OSPFv3, IS_IS, BGP4, EIGRP, BABEL, BFD, VRRP, PIM, OpenFabric, OpenFlow, P4Runtime, NETCONF, RESTCONF, GNMI, BGPLS };
enum class Scope { Local, Site, AutonomousSystem, InterDomain, Overlay };
struct Prefix { std::string cidr; AddressFamily family{AddressFamily::IPv4}; };
struct NextHop { std::string address; std::string interface; };
struct Route { Prefix prefix; NextHop next_hop; Protocol protocol{Protocol::Static}; std::uint32_t metric{0}; std::uint32_t admin_distance{1}; std::uint64_t expires_at_ms{0}; bool recursive{false}; };
class RouteTable {
  std::vector<Route> routes_;
public:
  bool add(Route route) { routes_.push_back(std::move(route)); return true; }
  bool remove(const std::string& cidr) { auto old=routes_.size(); routes_.erase(std::remove_if(routes_.begin(),routes_.end(),[&](const Route&r){return r.prefix.cidr==cidr;}),routes_.end()); return old!=routes_.size(); }
  std::optional<Route> best(const std::string& cidr) const { std::optional<Route> result; for (const auto& r: routes_) if (r.prefix.cidr==cidr && (!result || r.admin_distance<result->admin_distance || (r.admin_distance==result->admin_distance && r.metric<result->metric))) result=r; return result; }
  const std::vector<Route>& all() const { return routes_; }
};
struct RoutingCapabilities {
  AddressFamily address_family{AddressFamily::DualStack};
  std::vector<Protocol> protocols{
    Protocol::Static, Protocol::Connected, Protocol::RIP, Protocol::RIPng,
    Protocol::OSPFv2, Protocol::OSPFv3, Protocol::IS_IS, Protocol::BGP4,
    Protocol::EIGRP, Protocol::BABEL, Protocol::BFD, Protocol::VRRP,
    Protocol::PIM, Protocol::OpenFabric, Protocol::BGPLS,
    Protocol::OpenFlow, Protocol::P4Runtime, Protocol::NETCONF,
    Protocol::RESTCONF, Protocol::GNMI
  };
  bool hardware_offload{false};
  bool software_defined{true};
};
class RoutingEngine { public: virtual ~RoutingEngine() = default; virtual bool start() = 0; virtual void stop() = 0; virtual bool advertise(const Route&) = 0; virtual bool withdraw(const Prefix&) = 0; };
}
